from django.urls import path
from . import views 




app_name = 'Customer'
urlpatterns = [
    
    path('', views.Home.as_view(), name='home'),
    path('search/', views.search_view, name='search' ),
    path('Customer/<int:pk>/', views.CustomerView.as_view(), name='customerview'),
    path('reg/logout', views.logout_sys, name='logout_user')

]
