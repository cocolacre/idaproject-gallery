#https://www.geeksforgeeks.org/python-uploading-images-in-django/
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        #fields=['image']
        fields=["name", 'image']

#TODO: class CustomImageForm(forms.ModelForm):