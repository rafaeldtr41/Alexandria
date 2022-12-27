from django import forms
from .models import *
from django.db.models import F
from django.utils import timezone




CHOICES = [

        ('C', 'Clientes'),
        ('B', 'Libros'),
        ('A', 'Autores')
]


class search_home(forms.Form):

    name = forms.CharField(label='search-bar', max_length=150)


class add_prestamof(forms.ModelForm):

        def __init__(self, *args, **kwargs):

                self.clienteid = kwargs.pop('cliente', None)
                super(add_prestamof, self).__init__(*args, **kwargs)

                #HTML atributes 
                self.fields['books'].widget.attrs['class'] = 'select'
                self.fields['books'].widget.attrs['name'] = 'libros'
                
                self.fields['cant'].widget.attrs['class'] = "input--style-4"
                self.fields['cant'].widget.attrs['type'] = "text"
                self.fields['cant'].widget.attrs['name'] = "Nombre"

        class Meta:

                model = prestamo
                exclude = ('devuelto','cliente', 'date')

        def save(self, commit=True):

                aux = Cliente.objects.get(id=self.clienteid)
                form = super().save(commit=False)
                form.cliente = aux
                form.date = timezone.now()

                if commit :

                        form.save()
                return form



class AddClienteForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):

                super(AddClienteForm, self).__init__(*args, **kwargs)

                # HTML atributos 
                self.fields['foto'].widget.attrs['type'] = 'file'
                self.fields['foto'].widget.attrs['class'] = "form-control d-none"
                self.fields['foto'].widget.attrs['id'] = "customFile2"

                self.fields['nombre'].widget.attrs['class'] = "input--style-4"
                self.fields['nombre'].widget.attrs['type'] = "text"
                self.fields['nombre'].widget.attrs['name'] = "Nombre"

                self.fields['apellidos'].widget.attrs['class'] = "input--style-4"
                self.fields['apellidos'].widget.attrs['type'] = "text"
                self.fields['apellidos'].widget.attrs['name'] = "Apellidos"

                self.fields['CI'].widget.attrs['class'] = "input--style-4"
                self.fields['CI'].widget.attrs['type'] = "text"
                self.fields['CI'].widget.attrs['name'] = "Carnet de Identidad"

                self.fields['solapin'].widget.attrs['class'] = "input--style-4"
                self.fields['solapin'].widget.attrs['type'] = "text"
                self.fields['solapin'].widget.attrs['name'] = "solapin"

                self.fields['facultad'].widget.attrs['name'] = "Facultad"

        class Meta:

                model = Cliente
                fields = '__all__'
