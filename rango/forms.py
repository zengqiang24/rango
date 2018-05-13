from django import forms
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes=forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug=forms.IntegerField(widget=forms.HiddenInput(), required=False)

    # A inline class to provide additional information on the form
    class Meta:
          model=Category
          fields=('name',)



class PageForm:
    title=forms.CharField(max_length=128,help_text="please enter the title of ")
    url= forms.URLField(max_length=200,help_text="please enter the url of page.")
    views=forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model=Page
        exclude=('category',)