from django.urls import path
from . import views




app_name = "background"
urlpatterns = [
    
    path('error/404', views.View_404, name='404'),
    path('error/403', views.View_403, name='403'),
]
