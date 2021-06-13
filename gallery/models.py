from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=512)
    
    ### upload to MEDIA_ROOT/uploads
    image = models.ImageField(upload_to = "uploads", max_length=512,default="placeholder_name.png")
    # TODO: improve default value?
    url = models.CharField(max_length=1024, default="")
    #https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png
    
#Q: What if we delete image file?
#Q: What if filename already exist?
#TODO: filename checks and optional modification
#TODO: Test.
#Q: What if image upload process fails?
#   TODO: Test this.
#NOTE: It is mandatory for the HTML form 
#   to have the attribute `enctype="multipart/form-data"`    
#Q: What if we work in Windows user filesystem from WSL?
#A: We needed to move project to WSL fs and chown recursively.
#    sudo chown -R cocolacre /home/cocolacre/
class ResizedImage(models.Model):
    original = models.ForeignKey(Image, on_delete = models.CASCADE,default="placeholder_name_resized.png")
    #TODO: Improve\remove default placeholder_name.
    name_resized = models.CharField(max_length=512)
    image_resized = models.ImageField(upload_to = "resized_uploads", max_length=512,default="resized_placeholder_name.png")
    