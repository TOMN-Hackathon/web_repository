from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    messages_dict = file.open()
    return HttpResponse("<p>Hello World</p>",content_type="text/html")

def user(request):
    pass

def messages(request):
    pass 

def ai(request):
    pass