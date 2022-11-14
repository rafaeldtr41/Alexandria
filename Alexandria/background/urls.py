from django.urls import path
from . import views




app_name = "background"
urlpatterns = [
    
    path('register/send', views.sender, name='Email'),
]
