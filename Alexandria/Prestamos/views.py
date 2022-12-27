from django.template import loader
from django.views import generic
from Books.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from Books.models import Book
from django.urls import reverse_lazy
from django.db.models import F
from itertools import chain
from django.shortcuts import get_object_or_404, redirect




class Home(LoginRequiredMixin, generic.ListView):

    template_name = 'Customer/Home.html'
    login_url = 'users_regs:login'
    context_object_name = 'cliente_list'
    
    def get_queryset(self) :
    
        return Cliente.objects.all()

"""
class list_cliente(LoginRequiredMixin, generic.ListView):
    
    template_name = ''

   """
   
    
class list_prestamo(LoginRequiredMixin, generic.ListView):

    template_name = 'Customer/Search.html'
    context_object_name = 'prestamo_list'

    def get_queryset(self) :

        return prestamo.objects.get(devuelto=True)


class add_prestamo(LoginRequiredMixin, generic.CreateView):

    template_name = 'Customer/PrestamoForm.html'
    form_class =  add_prestamof 
    success_url = reverse_lazy('Prestamos:home')

    def get_form_kwargs(self):
        
        dict  = super().get_form_kwargs()
        dict['cliente'] = self.request.session['cliente']
        return dict

    def form_valid(self, form):

        aux = Book.objects.get(id=form.cleaned_data['books'].id)
        cant = aux.cant_ejemplares - aux.cant_prestado - form.cleaned_data['cant']
        if cant < 0:
            
            return super().form_invalid(form)

        aux.cant_prestado = F('cant_prestado') + form.cleaned_data['cant']
        aux.save()
        form.save()    
        return super().form_valid(form)


@login_required
def delete_prestamo (request, pkey):

    prest = get_object_or_404(prestamo, pk=pkey)
    prest.delete()
    return redirect('Prestamos:home')


class detail_cliente (LoginRequiredMixin,generic.DetailView):
    
    model = Cliente
    template_name = 'Customer/Cliente.html'
    
    def get_context_data(self, **kwargs):
        
        dict = super().get_context_data(**kwargs)
        try:
            aux1 = prestamo.objects.only('id','books', 'date').filter(cliente=self.object, devuelto=False)
            dict['datos'] = aux1
        except (prestamo.DoesNotExist):

            dict['mensaje'] = 'No existen prestamos'

        self.request.session['cliente'] = self.object.id
        return dict


class AddCliente(LoginRequiredMixin, generic.CreateView):

    template_name = 'Customer/clienteform.html'
    form_class = AddClienteForm
    success_url = reverse_lazy('Prestamos:home')
