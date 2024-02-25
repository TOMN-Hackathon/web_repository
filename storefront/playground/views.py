from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    #messages_dict = file.open()
    return render(request, "index.html")

def user(request):
    print(request)

def messages(request):
    pass 

def ai(request):
    pass