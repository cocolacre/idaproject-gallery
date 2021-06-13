from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImageForm

def index(request):
    return HttpResponse("This is alpha gallery app with image resizer for Idaproject interview attempt.")

def image_list(request):
    return render(request, "image_list.html")

def resizing_result(request):
    return render(request,"resizing_result.html")


def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid(): #TODO: заменить на проверку соответствия заданию.
            form.save()
            return redirect("success")#Q: Is "name" kwarg of django.urls.path used here?
    else:
        #Here we recieve GET request,then return an HttpResponse 
        #object with the result of the rendered template (1.html)
        form = ImageForm()
        #
    return render(request, "upload_image.html",{"form":form})

def success(request):
    return HttpResponse("successfully uploaded")