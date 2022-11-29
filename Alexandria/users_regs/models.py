from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class LibreriaUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.CharField(max_length=11, default='')
    imagen = models.ImageField(upload_to='Images/Usuarios', default='Images/Usuarios/default.png')
    solapin =  models.CharField(max_length=7, default='')


class ConfirmedEmails(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=True)
