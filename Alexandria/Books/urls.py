from django.urls import path
from . import views




app_name = 'Books'
urlpatterns = [
    
    
    path('listbook', views.book_list.as_view(), name='listbook'),
    path('bookdetail/<int:pk>', views.BookView.as_view(),name='bookdetail'),

]

