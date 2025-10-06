from django.urls import path
from .views import home_view, about_view

urlpatterns = [
    path("hello/", home_view, name="hello_home"),
    path("about/", about_view, name="hello_about"),
]