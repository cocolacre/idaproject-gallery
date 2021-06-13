from django.shortcuts import render
from django.http import HttpResponse
from forms import *

# Create your views here.

def index(request):
    return HttpResponse("This is a gallery app with image resizer for Idaproject")

def image_view(request):
    if request.method = "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ImageForm()
    return render(request, "1.html",{"form":form})

def success(request):
    return HttpResponse("successfully uploaded")