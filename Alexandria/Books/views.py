from django.shortcuts import render
from django.template import loader
from .models import Book, Author, Category
# from Prestamos.models import Customer, Prestamo
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from Prestamos.models import prestamo




class BookView(LoginRequiredMixin, generic.DetailView):

    model = Book
    template_name =  'Books/BookView.html'

    def get_context_data(self, **kwargs):
        
        dict  = super().get_context_data(**kwargs)
        try:
            dict['prestamo'] = prestamo.objects.filter(books=self.object, devuelto=False)
        except prestamo.DoesNotExist:
            dict['mensaje'] = "No hay prestamos :("
        return dict


class book_list(LoginRequiredMixin , generic.ListView):
    
    template_name = 'Customer/Libros.html'
    context_object_name= 'booklist'

    def get_queryset(self):

        return Book.objects.all().order_by('-cant_prestado')
