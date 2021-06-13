from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=512)
    
    ### upload to MEDIA_ROOT/uploads
    image = models.ImageField(upload_to = "uploads/", max_length=512,default="1.png")
    # TODO: improve default value?
    
#Q: What if we delete image file?
#Q: What if filename already exist?
#TODO: filename checks and optional modification
#Q: What if image upload process fails?
#   TODO: Test this.
#NOTE: It is mandatory for the HTML form 
#   to have the attribute `enctype="multipart/form-data"`    
#Q: What if we work in Windows user filesystem from WSL?
#A: We needed to move project to WSL fs and chown recursively.
#    sudo chown -R cocolacre /home/cocolacre/
class ResizedImage(models.Model):
    original = models.ForeignKey(Image, on_delete = models.CASCADE,default="1")
    name = models.CharField(max_length=512)
    image = models.ImageField(upload_to = "resized_uploads/", max_length=512,default="1.png")
    