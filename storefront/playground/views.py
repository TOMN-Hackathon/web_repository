from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    #messages_dict = file.open()
    return render(request, "index.html")

def user(request):
	userMessage= request.GET.get("userMessage", "")
	return HttpResponse(f"<span class='user-message'><p>{userMessage}</p></span>", content_type="text/html")

def messages(request):
    pass

def ai(request):
    pass
