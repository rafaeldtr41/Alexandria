from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views import generic
from .forms import search_form
from .models import Customer, CustomerFilter, Prestamo
from Books.models import Book, Author, AuthorFilter
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout





class Home(LoginRequiredMixin, generic.TemplateView):

    template_name = 'Customer/index.html'


class Search(LoginRequiredMixin, generic.ListView):

    template_name = 'Customer/Search.html'


@login_required(redirect_field_name='account/login')
def search_view(request):
    
    dict = {}
    f = None
    clase = ''
    if request.method == 'POST':

        form = search_form(request.POST)
        if form.is_valid():

            if form.fields['table'] == 'C': #Customer Search

                f = CustomerFilter(request, value=form.fields['value'])
                clase = 'C'
            elif form.fields['table'] == 'B': # Book Search

                f = Book.objects.filter(name__icontains=form.fields['value'])
                clase = 'B'
            else:   #Author Search
                
                f = AuthorFilter(request, value=form.fields['value'])
                clase = 'A'

    dict['search'] = f
    dict['class'] = clase
    return render(request, 'Customer/Search.html', dict)
        

class CustomerView(LoginRequiredMixin, generic.DetailView):

    model = Customer
    template_name = 'Customer/CustomView.html'

    def get_context_data(self, **kwargs):
        
        dict =  super().get_context_data(**kwargs)
        aux = Prestamo.objects.only('book').filter(Customer=self.object.id)
        aux = Book.objects.filter(id__in=aux)
        dict['books'] = aux
        return dict


def logout_sys(request):

    if request.user.isauthenticated():

        logout(request)
    
    return redirect('/account/login')
