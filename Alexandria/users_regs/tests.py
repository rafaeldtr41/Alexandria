from django.test import TestCase
from django.urls import reverse
from django.shortcuts import redirect
from django.test import Client
from django.contrib.auth.models import User




class UserRegTest(TestCase):

    def setUp(self):
       
        User.objects.create(username='pablo1', password='12345678')
        self.c = Client()
        

    def test_redirect_from_login_to_create(self):

        response = self.client.get(reverse('/accounts/login'))
        response.client.get(reverse('users_regs:Register'))
        self.assertEqual(response.status_code, 200)

    def test_go_from_login_authenticated(self):

        self.c = Client()
        self.c.login(username='pablo1', password='12345678')
        response = self.c.get(reverse('accounts/login'))
        self.assertEqual(response.status_code, 300)

    def test_go_from_login_to_add_info(self):

        self.c.get(reverse('accounts/login'))
        response = self.c.get(reverse('users_regs:add_info'))
        self.assertEqual(response.status_code, 300)

    def test_go_from_login_to_add_libuser(self):

        self.c.get(reverse('accounts/login'))
        response = self.c.get(reverse('users_regs:add_info'))
        self.assertEqual(response.status_code, 300)

    def test_go_from_login_to_Mail(self):

        self.c.get(reverse('accounts/login'))
        response = self.c.get(reverse('users_regs:Mail'))
        self.assertEqual(response.status_code, 300)

    def test_go_from_home_to_Mail(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse(''))
        response = self.c.get(reverse('users_regs:Mail'))
        self.assertEqual(response.status_code, 300)
    
    def test_go_from_home_to_add_libuser(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse(''))
        response = self.c.get(reverse('users_regs:add_libuser'))
        self.assertEqual(response.status_code, 300)

    def test_go_from_home_to_add_info(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse(''))
        response = self.c.get(reverse('users_regs:add_info'))
        self.assertEqual(response.status_code, 300)

    def test_go_from_home_to_create(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse(''))
        response = self.c.get(reverse('users_regs:register'))
        self.assertEqual(response.status_code, 300)
    
    def test_go_from_home_to_add_login(self):

        self.c.login(username='pablo1', password='12345678')
        self.c.get(reverse(''))
        response = self.c.get(reverse('accounts/login'))
        self.assertEqual(response.status_code, 300)
