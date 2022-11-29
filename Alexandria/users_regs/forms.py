from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import LibreriaUser
from django.utils import timezone




class UserForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())    

    class Meta:

        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )
    
    def save(self, commit=True):

        user = super(UserForm, self).save(commit=False)
        user.date_joined = timezone.now()
        user.is_staff = False
        user.is_active = False
        user.is_superuser = False
        user.last_login = timezone.now()
        user.password = self.cleaned_data['password1']
        if commit:

            user.save()
        return user.username
    
    
class LibraryUserForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(LibraryUserForm, self).__init__(*args, **kwargs)

    class Meta:

        model = LibreriaUser
        exclude = ['user']

    def save(self, commit=True):

        user = super(LibraryUserForm, self).save(commit=False)
        user.user = self.user
        if commit:
            
            user.save()

        
class UserFormSInfo(forms.Form):

    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

    def save(self, user):

        aux = User.objects.get(username=user)
        aux.first_name = self.cleaned_data['first_name']
        aux.last_name = self.cleaned_data['last_name']
        aux.email = self.cleaned_data['email']
        aux.save()


class ConfirmEmail(forms.Form):

    code = forms.CharField(max_length=6, required=True)


class Login(forms.Form):

    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
