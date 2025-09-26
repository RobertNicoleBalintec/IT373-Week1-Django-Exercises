from django.urls import path
from .views import home_view, about_view

urlpatterns = [
    path("hello/", home_view),
    path("about/", about_view),
]