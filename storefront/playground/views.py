from django.shortcuts import render
from django.http import HttpResponse
import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Create your views here.
def landing(request):
    return render(request, "index.html")

def add_to_json(user, message):
    with open('storefront/playground/templates/message.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    data_file.close()
    data.append({"role":user, "content" :message})
    with open('storefront/playground/templates/message.json', 'w') as data_file:
        json.dump(data, data_file)
    data_file.close()



def user(request):
    userMessage = request.GET.get("userMessage", "")
    add_to_json("user", userMessage)
    return HttpResponse(f"<span class='user-message' hx-get='/ai' hx-target='#ai-message' hx-trigger='load'><p>{userMessage}</p></span>", content_type="text/html")

def messages(request):
    with open('storefront/playground/templates/message.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    data_file.close()
    json_d_data = json.dumps(data)
    return json_d_data


def ai(request):
    with open('storefront/playground/templates/message.json', encoding='utf-8') as data_file:
        history = json.loads(data_file.read())
    data_file.close()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=history
    )

    reply = completion.choices[0].message.content
    add_to_json("assistant", reply)
    return HttpResponse(f"<span class='ai-message'><p>{reply}</p></span>", content_type="text/html")
