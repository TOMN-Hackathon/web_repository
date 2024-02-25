from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.landing),
    path("user/", views.user),
    path("messages/", views.messages),
    path("ai/", views.ai)
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
