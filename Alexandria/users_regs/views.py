from django.conf import settings
from django.template import loader
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse
from .models import ConfirmedEmails
from . import forms
from . import models
import datetime
import os
import random




class register(generic.FormView):

    template_name = "registration/newuser.html"
    form_class = forms.UserCreationForm
    success_url = '/register/add_info'
    

    def form_valid(self, form):

        aux = form.save()
        login(self.request, aux)
        return super().form_valid(form)


class AddInfo(LoginRequiredMixin, generic.FormView):

    template_name = "registration/names.html"
    form_class = forms.UserFormSInfo
    success_url = '/register/add_lib'

    def form_valid(self, form):
        
        form.save(self.request.user.username)
        return super().form_valid(form)


def AddLibraryUser(request):

    if request.method == 'POST':

        form = forms.LibraryUserForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():

            form.save()
            return redirect('users_regs:Email')

    form = forms.LibraryUserForm(user=request.user)
    return render(request, 'registration/lib.html', {"form":form})


class ConfirmEmail(LoginRequiredMixin, generic.FormView):

    template_name = "registration/confemail.html"
    form_class = forms.ConfirmEmail
    success_url = '/register/confirm'

    def form_valid(self, form):

        aux = self.get_context_data()
        aux1 = datetime.timedelta(minutes=5)
        if timezone.now().date() - aux['time'] < aux1:

            if form.cleaned_data['code'] == aux['code']:
                
                ConfirmedEmails.objects.create(User.objects.only('id')
                .get(self.request.user.username).id, True)
                return super().form_valid(form)

            messages.error(self.request, "Codigo incorrecto")

        messages.error(self.request, "Codigo vencido por favor reenvie el mensaje")      

def asign_random():

    return str(random.randint(100000, 999999))


def sender(request):

    aux = asign_random()
    send_mail(
        subject='Please Confirm Your email',
        message='the code to login is: ' + aux + ". \n Dont share it, if it wasn't you please go to" + 
        " link below \n" + "www.fakeorg.com",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    
    return redirect(reverse('users_regs:confirm_mail', {"code": aux, "time":timezone.now().date()}))
