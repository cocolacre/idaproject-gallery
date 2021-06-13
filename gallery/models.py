from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=512)
    image = models.ImageField(max_length=512)
#what if we delete image file?
#what if filenames are duplicated?
#what if image load fails?


class ResizedImage(models.Model):
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    resized_image_filename = models.CharField(max_length=512)
