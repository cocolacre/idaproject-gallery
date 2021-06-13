#https://www.geeksforgeeks.org/python-uploading-images-in-django/
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields=['name','image']