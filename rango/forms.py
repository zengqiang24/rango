from django import forms
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="please enter the category name.")
    views = forms.IntegerField(weight=forms.HiddenInput(), initital=0)
