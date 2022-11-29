from django.conf import settings
from django.template import loader
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
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




def register(request):

    if  not request.user.is_authenticated:

        if request.method == 'POST':

            form = forms.UserForm(request.POST)

            if form.is_valid():


                
                username = form.save()
                return redirect(reverse('users_regs:add_libuser', {'username':username}))

        form = forms.UserForm()
        return render(request, "registration/newuser.html", {'form': form})
    
    return redirect('background:403')
    

def AddLibraryUser(request):

    dict = request.GET
    if request.META.get('HTTP_REFERER') == '/register' and not request.user.is_authenticated and 'username' in dict:

        dict = request.GET
        if request.method == 'POST':

            form = forms.LibraryUserForm(request.POST, request.FILES, user=dict['username'])
            if form.is_valid():

                form.save()
                return redirect('Prestamos:home', dict)

        dict['form'] = forms.LibraryUserForm(user=None)
        return render(request, 'registration/lib.html', dict)

    return redirect('background:403')


def ConfirmEmail(request):

    aux = datetime.timedelta(minutes=5)
    dict = request.GET
    if request.META.get('HTTP_REFERER') == '/register/send' and 'username' in dict and not request.user.is_authenticated:
        
        user = User.objects.get(username=dict['username'])

        if user is not None:
        
            if request.method == 'POST' and user is not None:
    
                form = forms.ConfirmEmail(request.POST)
            
                if form.is_valid():
                
                    if timezone.now.date() - dict['time'] < aux and form.cleaned_data['code'] == dict['code']:
                    
                        ConfirmedEmails.objects.create(user.id, True)
                        login(request, user)
                        messages.success(request, 'Redireccionando')
                        return redirect('Prestamos:home', dict)
                     
                    messages.error(request, "Codigo erroneo o tiempo excedido")

            dict['form'] =  forms.ConfirmEmail()
            return render(request, "registration/confemail.html", dict)
    
    return redirect('background:403')
      

def asign_random():

    return str(random.randint(100000, 999999))


def sender(request):

    dict = request.GET
    if not request.user.is_authenticated and (request.META.get('HTTP_REFERER') == '/register/add_lib' or request.META.get('HTTP_REFERER') == '/register/confirm') and 'username' in dict:
       
        
        
        user = User.objects.only('email').get(username=dict['username'])

        if user is not None:
            
            aux = str(asign_random())
            send_mail(
                subject='Please Confirm Your email',
                message='the code to login is: ' + aux + ". \n Dont share it, if it wasn't you please go to" + 
                " link below \n" + "www.fakeorg.com",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
        
            dict["code"] = aux
            dict["time"] = timezone.now().date()
            return redirect(reverse('users_regs:confirm_mail', dict))

    return redirect('background:403')


def Login_view(request):

    if not request.user.is_authenticated:

        if request.method == 'POST':

            form = forms.Login(request.POST)

            if form.is_valid():

                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

                if user is not None:

                    login(request, user)
                    messages.success(request, 'redireccionando')
                    return redirect('Prestamos:home')
                
                messages.error(request, 'Usuario o contraseña incorrecta')
                return redirect('users_regs:login')

        form = forms.Login()
        return render(request, 'registration/login.html', {'form':form})

    return redirect('background:403')
