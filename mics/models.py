from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'static/img/')
    image_url = models.TextField(blank = True)
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    
