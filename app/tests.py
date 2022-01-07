from django.test import TestCase
from app.forms import TitleForm
from app.models import GuestModel


class MyTests(TestCase):
    def test_call_view(self):
        response1 = self.client.post("/")
        self.assertEquals(response1.status_code, 200)

    def test_form(self):
        form_data = {"name": "UsualName"}
        form = TitleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_digits_and_symbols(self):
        form_data = {"name": "@qwerty1!^"}
        form = TitleForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_with_model(self):
        form_data = {"name": "tesTguesT"}
        form = TitleForm(data=form_data)
        self.assertTrue(GuestModel.objects.create(name=form.data["name"]))
        model = GuestModel.objects.filter(name=form.data["name"]).exists()
        self.assertTrue(model)
