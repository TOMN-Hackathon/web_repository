from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.landing)
    path("user/", view.user)
    path("messages/", view.messages)
    path("ai/", view.ai)
]