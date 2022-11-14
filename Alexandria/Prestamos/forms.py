from django import forms




CHOICES = [

        ('C', 'Clientes'),
        ('B', 'Libros'),
        ('A', 'Autores')
]


class search_form(forms.Form):

    value = forms.CharField(label='search-bar', max_length=150)
    table = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
