# forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class PasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise ValidationError("User with this username does not exist.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError("Passwords do not match.")
        return cleaned_data
