from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'static/img/')
    image_url = models.TextField(blank = True)
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def image_list(cls):

        images = cls.objects.all()
        return images
    @classmethod
        def search_by_category(cls,searched_category):
            images = cls.objects.filter(image_location__category__icontains = searched_category)
            return images

    @classmethod
        def filter_by_location(cls,searched_location):
            images=cls.objects.filter(image_location__category__icontains = searched_location)


class Location(model.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.Location

    def save_location(self):
        self.save()

class Category(model.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()
