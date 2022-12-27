from django.urls import path
from . import views 




app_name = 'Prestamos'
urlpatterns = [
    
    path('', views.Home.as_view(), name='home'),
    #path('cliente/', views.list_cliente.as_view(),name='lcliente'),
    path('prestamos/', views.list_prestamo.as_view(),name='lprestamo'),
    #path('prestamo_detail/', views.detail_prestamo.as_view(),name='dprestamo'),
    path('add_prestamo/', views.add_prestamo.as_view(),name='addprestamo'),
    path('delete_prestamo/<int:pkey>/', views.delete_prestamo,name='delprestamo'),
    path('cliente_detail/<int:pk>/', views.detail_cliente.as_view(),name='dcliente'),
    path('add_cliente/', views.AddCliente.as_view(), name='addc'),

]