from django import forms




CHOICES = [

        ('C', 'Clientes'),
        ('B', 'Libros'),
        ('A', 'Autores')
]


class search_home(forms.Form):

    name = forms.CharField(label='search-bar', max_length=150)
    
