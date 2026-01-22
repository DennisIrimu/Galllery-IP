from django.contrib import admin

from .models import Image, Location, Category, Tag, Profile, Comment

# Register your models here.
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Comment)