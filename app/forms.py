from django.forms import ModelForm
from app.models import GuestModel
from django import forms


class TitleForm(ModelForm):
    name = forms.CharField(
        error_messages={"unique": "This name is already exists =("},
        widget=forms.TextInput(attrs={"placeholder": ("No symbols and digits")}),
    )

    class Meta:
        model = GuestModel
        fields = ["name"]

    def clean_name(self):
        guest = self.cleaned_data.get("name")
        if not guest.isalpha():
            raise forms.ValidationError("Name must contains only letters!")
        return guest.lower()
