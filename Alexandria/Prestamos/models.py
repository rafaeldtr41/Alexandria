from django.db import models
from Books.models import Book




class Cliente (models.Model):
    
    CHOICE = (
        ('1', 'FACULTAD1'),
        ('2', 'FACULTAD2'),
        ('3', 'FACULTAD3'),
        ('4', 'FACULTAD4'),
        ('5', 'FACULTAD5'),
        ('6', 'FACULTAD6'),
    )
    foto = models.ImageField(upload_to='Images/Cliente', default='Images/Cliente/default.png')
    nombre = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    CI = models.CharField(max_length=11)
    solapin = models.CharField(max_length=7)
    facultad = models.CharField(max_length=120,choices=CHOICE)

    def __str__(self):
        
        return self.nombre + ' ' + self.apellidos 


class prestamo (models.Model):

    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField()
    cant = models.IntegerField(default=1)
    devuelto = models.BooleanField(default=False)
