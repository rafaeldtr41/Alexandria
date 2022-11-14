from django.db import models
from django.db.models import Q
from Books.models import Book
import django_filters



 
class Customer(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    ci = models.CharField(max_length=11)
    solapin = models.CharField(max_length=7)
    
    def class_type(self):

        return 'Customer'
    




class Prestamo(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class CustomerFilter(django_filters.FilterSet):

    class Meta:
        
        model = Customer
        fields = [
            
            'first_name',
            'last_name',
            'ci',
            'solapin',
            ]

    def custom_filter(self, queryset, name, value):

        value = value.split()
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(ci__icontains=value)
            | Q(solapin__icontains=value))
