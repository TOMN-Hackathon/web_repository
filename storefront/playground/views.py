from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return HttpResponse("<p>Hello World</p>",content_type="text/html")