from django.test import TestCase
from .models import Customer, Prestamo
from Books.models import Book
from django.utils import timezone
from .forms import search_form
from django.test import Client
from django.urls import reverse




class Test_Forms(TestCase):

    def test_form_work(self):

        form_data = {'value': 'Juan', 'table': 'C'}
        form = search_form(form_data)
        self.assertTrue(form.is_valid())

    def test_form_wrong_table_entry(self):

        form_data = {'value': 'Juan', 'table': 'S'}
        form = search_form(form_data)
        self.assertFalse(form.is_valid())

 
class ViewsTest(TestCase):

    def setUp(self) -> None:
        
        self.cliente  =  Client()

    def test_go_home_no_login(self):

        
        response = self.cliente.get('/')
        self.assertEqual(response.status_code, 302)

    def test_go_home_with_login(self):

        self.cliente.login('morpheus')
        response = self.cliente.get('/')
        self.assertEqual(response.status_code, 200)
