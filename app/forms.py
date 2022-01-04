from django.forms import ModelForm
from app.models import GuestModel
from django import forms


class TitleForm(ModelForm):
    class Meta:
        model = GuestModel
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Without digits and symbols"}
            )
        }

    def clean_name(self):
        guest = self.cleaned_data.get("name")
        if guest.isalpha():
            return guest
