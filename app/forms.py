from app.models import GuestModel
from django import forms


class TitleForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": ("No symbols and digits")}),
    )

    def clean_name(self):
        guest = self.cleaned_data["name"]
        if not guest.isalpha():
            raise forms.ValidationError("Name must contains only letters!")
        return guest.lower()

    def save(self, name):
        return GuestModel.objects.create(name=name)
