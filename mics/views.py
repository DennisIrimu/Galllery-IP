import os

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import (
    SignUpForm,
    ImageForm,
    CategoryForm,
    LocationForm,
    TagForm,
    CommentForm,
    ProfileForm,
)
from .models import Image, Category

# Create your views here.

def image_list(request):
    images = (
        Image.objects.select_related("image_category", "image_location", "created_by")
        .prefetch_related("tags", "likes", "created_by__profile")
        .all()
    )
    story_user_ids = (
        Image.objects.exclude(created_by=None)
        .order_by("-created_at")
        .values_list("created_by", flat=True)
        .distinct()[:8]
    )
    story_users = (
        User.objects.filter(id__in=list(story_user_ids))
        .select_related("profile")
        .order_by("username")
    )
    return render(
        request,
        "index.html",
        {"images": images, "story_users": story_users},
    )


def search_results(request):
    if "image_category" in request.GET and request.GET["image_category"]:
        searched_category = request.GET.get("image_category")
        images = Image.search_by_category(searched_category)
        message = f"{searched_category}"
        return render(request, "search.html", {"message": message, "images": images})

    message = "No results found."
    return render(request, "search.html", {"message": message})

def image(request, image_id):
    image_obj = get_object_or_404(
        Image.objects.select_related("image_category", "image_location", "created_by")
        .prefetch_related("tags", "likes", "comments__user__profile"),
        id=image_id,
    )
    comments = image_obj.comments.select_related("user", "user__profile").order_by(
        "-created_at"
    )
    return render(
        request,
        "image.html",
        {"image": image_obj, "comments": comments, "comment_form": CommentForm()},
    )


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("indexImages")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


@login_required
def create_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save(commit=False)
            image_obj.created_by = request.user
            if image_obj.image and not image_obj.image_name:
                name = os.path.splitext(os.path.basename(image_obj.image.name))[0]
                image_obj.image_name = name.replace("-", " ").replace("_", " ").title()
            image_obj.save()
            form.save_m2m()
            return redirect("indexImages")
    else:
        form = ImageForm()
    return render(request, "create_image.html", {"form": form})


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect("indexImages")
    else:
        form = CategoryForm()
    return render(request, "create_category.html", {"form": form})


@login_required
def create_location(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.created_by = request.user
            location.save()
            return redirect("indexImages")
    else:
        form = LocationForm()
    return render(request, "create_location.html", {"form": form})


@login_required
def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.created_by = request.user
            tag.save()
            return redirect("indexImages")
    else:
        form = TagForm()
    return render(request, "create_tag.html", {"form": form})


@login_required
def like_image(request, image_id):
    image_obj = get_object_or_404(Image, id=image_id)
    if request.user in image_obj.likes.all():
        image_obj.likes.remove(request.user)
    else:
        image_obj.likes.add(request.user)
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/"
    return redirect(next_url)


@login_required
def add_comment(request, image_id):
    image_obj = get_object_or_404(Image, id=image_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image_obj
            comment.save()
    return redirect("viewImage", image_id=image_id)


def profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    images = (
        Image.objects.filter(created_by=user_obj)
        .select_related("image_category", "image_location", "created_by")
        .prefetch_related("tags", "likes")
        .order_by("-created_at")
    )
    liked_images = (
        Image.objects.filter(likes=user_obj)
        .select_related("image_category", "image_location", "created_by")
        .prefetch_related("tags", "likes")
        .order_by("-created_at")[:6]
    )
    return render(
        request,
        "profile.html",
        {
            "profile_user": user_obj,
            "images": images,
            "liked_images": liked_images,
        },
    )


@login_required
def edit_profile(request):
    profile_obj = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        if form.is_valid():
            form.save()
            return redirect("profile", username=request.user.username)
    else:
        form = ProfileForm(instance=profile_obj)
    return render(request, "edit_profile.html", {"form": form})
