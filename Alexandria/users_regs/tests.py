from django.test import TestCase
from django.urls import reverse
from django.shortcuts import redirect
from django.test import Client
from django.contrib.auth.models import User




class RedirectsTest(TestCase):

    def setUp(self):
       
        self.user = User.objects.create_user(username='pablo1', password='12345678', 
        email='fakemail@fakemail.fm')
        self.c = Client()
        
    def tearDown(self):

        self.user.delete()
        

    def test_redirect_from_login_to_create(self):

        response = self.client.get(reverse('users_regs:login'))
        response.client.get(reverse('users_regs:Register'))
        self.assertEqual(response.status_code, 200)

    def test_go_from_login_authenticated(self):

        self.c = Client()
        self.c.login(username='pablo1', password='12345678')
        response = self.c.get(reverse('users_regs:login'))
        self.assertRedirects(response, '/error/403')


    def test_go_from_login_to_add_libuser(self):

        self.c.get(reverse('users_regs:login'))
        response = self.c.get(reverse('users_regs:add_libuser'))
        self.assertRedirects(response, '/error/403')

    def test_go_from_login_to_Mail(self):

        self.c.get(reverse('users_regs:login'))
        response = self.c.get(reverse('users_regs:Mail'))
        self.assertRedirects(response, '/error/403')

    def test_go_from_home_to_Mail(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse('Prestamos:home'))
        response = self.c.get(reverse('users_regs:Mail'))
        self.assertRedirects(response, '/error/403')
    
    def test_go_from_home_to_add_libuser(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse('Prestamos:home'))
        response = self.c.get(reverse('users_regs:add_libuser'))
        self.assertRedirects(response, '/error/403')


    def test_go_from_home_to_create(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse('Prestamos:home'))
        response = self.c.get(reverse('users_regs:Register'))
        self.assertRedirects(response, '/error/403')
    
    def test_go_from_home_to_add_login(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse('Prestamos:home'))
        response = self.c.get(reverse('users_regs:login'))
        self.assertRedirects(response, '/error/403')


class LoginTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='pablo1', password='12345678', 
        email='correofalso@correofalso.cf')
        self.c = Client()

    def tearDown(self) -> None:
        
        self.user.delete()

    def test_login_user_exist(self):

        response = self.c.post('/login', {'username': 'pablo1',
         'password': '12345678'})
        return self.assertRedirects(response, '/')

    def test_login_user_not_exist(self):

        response = self.c.post('/login', {'username': 'django66666666666666666666',
         'password': 'looooooooooooool'})
        return self.assertRedirects(response, '/login')

    def test_login_user_wrong_user(self):

        response = self.c.post('/login', {'username': 'django6666666666666666666666',
         'password': '12345678'})
        return self.assertRedirects(response, '/login')

    def test_login_user_wrong_password(self):

        response = self.c.post('/login', {'username': 'pablo1',
         'password': 'yyyyyyyyyyyyyyyyyyyyyy'})
        return self.assertRedirects(response, '/login')


class EmailTest(TestCase):

    pass
