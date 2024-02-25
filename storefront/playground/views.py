from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def landing(request):
    #messages_dict = file.open()
    return render(request, "index.html")

def add_to_json(user, message):
    with open('thing.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    data_file.close()
    print(data)
    print(type(data))
    data.append({"role":user, "message" :message})
    print(data)
    with open('thing.json', 'w') as data_file:
        json.dump(data, data_file)
    data_file.close()



def user(request):
    userMessage = request.GET.get("userMessage", "")
    add_to_json("user", userMessage)
    return HttpResponse(f"<span class='user-message'><p>{userMessage}</p></span>", content_type="text/html")

def messages(request):
    pass

def ai(request):
    pass
