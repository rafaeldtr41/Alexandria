from django.urls import path
from . import views




app_name = 'Books'
urlpatterns = [
    
    
    path('Author/<int:pk>/', views.AuthorView.as_view(), name='authorview'),
    

]

