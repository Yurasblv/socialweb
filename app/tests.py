from django.test import TestCase
from django.urls import reverse
from app.forms import TitleForm

class MyTests(TestCase):


    def test_call_error(self):
        # header = {'X-Requested-With': 'XMLHttpRequest'}
        response = self.client.post(reverse('title'),{'name': '*uniquenAm31@'})
        print(TitleForm(response))
        self.assertTrue(TitleForm(response))
