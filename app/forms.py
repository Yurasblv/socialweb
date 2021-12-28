from django.forms import ModelForm
from app.models import GuestModel
from django import forms


class TitleForm(ModelForm):
    class Meta:
        model = GuestModel
        fields = ['name']

