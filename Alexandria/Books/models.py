from django.db import models
from django.db.models import Q




class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birth = models.DateField()
    date_death = models.DateField(default=None)

    def __str__(self):
        
        return self.first_name + ' ' + self.last_name

    def class_type(self):

        return 'Author'


class Category(models.Model):

    name = models.CharField(max_length=100)
    Description  = models.TextField()

    def __str__(self):

        return 'Category'


class Book(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    cant_ejemplares = models.IntegerField()
    cant_prestado = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def class_type(self):

        return 'Book'

    def __str__(self):

        return self.name
