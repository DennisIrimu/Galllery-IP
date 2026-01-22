from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Image, Category, Location, Tag, Comment, Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            "image",
            "image_category",
            "image_location",
            "tags",
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("category",)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ("location",)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar", "bio")
