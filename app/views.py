from django.shortcuts import render
from django.http import HttpResponse
from . models import Places

# Create your views here.

def fun(request):
    obj=Places.objects.all()
    return render(request,"index.html",{'result':obj})

def contact(request):
    return render(request, "contact.html")

def news(request):
    return render(request, "news.html")
