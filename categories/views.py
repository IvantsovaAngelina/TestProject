from django.shortcuts import render
from .models import Categories

def home(request):
    categories = Categories.objects.all()
    return render(request, "categories/home.html", {'categories': categories})
