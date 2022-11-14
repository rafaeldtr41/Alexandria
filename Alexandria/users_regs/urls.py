from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




app_name = 'users_regs'
urlpatterns = [
    
   path('register', views.register.as_view(), name='Register'),
   path('register/add_info', views.AddInfo.as_view(), name='add_info'),
   path('register/add_lib', views.AddLibraryUser, name='add_libuser'),
   path('register/confirm', views.ConfirmEmail.as_view(), name='confirm_mail'),
   path('register/send', views.sender, name='Mail')

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
