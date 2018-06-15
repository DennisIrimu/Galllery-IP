from django.shortcuts import render
from .models import Image

# Create your views here.

def image_list(request):
    images = Image.image_list()
    return render(request, 'index.html',{"images":images})

def search_results(request):

    if 'image_category' in request.GET and request.GET["image_category"]:
        searched_category = request.GET.get("image_category")
        images = Image.search_by_category(searched_category)
        messages = f"{searched_category}"

        return render(request, 'search.html',{"message":message,"images":images,})
        
