from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.landing),
    path("user/", views.user),
    path("messages/", views.messages),
    path("ai/", views.ai)
]