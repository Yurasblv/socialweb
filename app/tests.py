from django.test import TestCase
from django.urls import reverse


class MyTests(TestCase):
    def test_call_error(self):
        data = {"name": "uniquenAm31@"}
        response = self.client.post(reverse("title"), data)
        self.assertEqual(response.json()["msg"], "Name must contains only letters!")

    def test_duplicate_error(self):
        data = {"name": "uniquenAme"}
        response = self.client.post(reverse("title"), data)
        self.assertEqual(response.json()["msg"], f"Hi {data['name']} =)")
        response2 = self.client.post(reverse("title"), data)
        self.assertEqual(response2.json()["msg"], f"{data['name']} exists yet =(")

    def test_different_letter(self):
        data = {"name": "Steven"}
        response = self.client.post(reverse("title"), data)
        self.assertEqual(response.json()["msg"], f"Hi {data['name']} =)")
        data = {"name": "sTeVeN"}
        response2 = self.client.post(reverse("title"), data)
        self.assertEqual(response2.json()["msg"], f"{data['name']} exists yet =(")
