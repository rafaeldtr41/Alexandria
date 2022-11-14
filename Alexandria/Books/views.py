from django.shortcuts import render
from django.template import loader
from .models import Book, Author, Category
from Prestamos.models import Customer, Prestamo
from django.views import generic
from django.contrib.auth.decorators import login_required




@login_required

class BookView(generic.DetailView):

    model = Book
    template_name =  'Books/BookView.html'

    def get_context_data(self, **kwargs):
        
        dict = super().get_context_data(**kwargs)
        aux = Prestamo.objects.only('Customer').filter(Book=self.object.id)
        aux = Customer.objects.filter(id__in=aux)
        dict['Cust'] = aux
        return dict


class AuthorView(generic.DetailView):

    model = Author
    template_name = "Book/AuthorView.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        aux = Book.objects.filter(author=self.object.id)
        context["Books"] = aux 
        return context    
