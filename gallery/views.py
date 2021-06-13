from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImageForm
from PIL import Image as Im
from .models import Image, ResizedImage


def index(request):
    return HttpResponse("This is alpha gallery app with image resizer for Idaproject interview attempt.")

def image_list(request):
    return render(request, "image_list.html")

def resizing_result(request):
    """
    >>>irs = ResizedImage.objects.all()[0]
    >>>irs.image_resized.path
        '/home/cocolacre/ida/media/resized_placeholder_name.png'
    """
    latest_image = Image.objects.order_by("-id")[0]
    #TODO: Improve. Obviously this is a bad idea to just use LATEST image - we might easily send userA's image to userB
    # in this situation.
    latest_image_resized = ResizedImage.objects.get(original_id=latest_image.id)
    
    context = {
               "latest_image" : latest_image,
               "latest_image_resized" : latest_image_resized
               }
    
    return render(request,"resizing_result.html", context)

def fail(request):
    return render(request,"fail.html")

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