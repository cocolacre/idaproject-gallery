from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=512)
    image = models.ImageField(upload_to = "uploads/", max_length=512,default="1.png")
    # file will be uploaded to MEDIA_ROOT/uploads
    
#what if we delete image file?
#what if filename already exist?
#   we need filename checks and optional modification
#what if image load fails?
#   (?) It is mandatory for the HTML form 
#   to have the attribute `enctype="multipart/form-data"`    
#what if we work in Windows user filesystem from WSL...

class ResizedImage(models.Model):
    original = models.ForeignKey(Image, on_delete = models.CASCADE,default="1")
    name = models.CharField(max_length=512)
    image = models.ImageField(upload_to = "resized_uploads/", max_length=512,default="1.png")
    