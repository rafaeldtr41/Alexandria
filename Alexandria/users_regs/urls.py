from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




app_name = 'users_regs'
urlpatterns = [
    
   path('register', views.register, name='Register'),
   path('register/add_lib', views.AddLibraryUser, name='add_libuser'),
   path('register/confirm', views.ConfirmEmail, name='confirm_mail'),
   path('register/send', views.sender, name='Mail'),
   path('login', views.Login_View.as_view(), name='login'),
   path('logout/', views.Logout, name='logout'),

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
