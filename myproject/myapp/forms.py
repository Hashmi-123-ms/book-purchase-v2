from django import forms
from .models import book


class book_form(forms.ModelForm):
    class Meta:
        model=book
        fields="__all__"