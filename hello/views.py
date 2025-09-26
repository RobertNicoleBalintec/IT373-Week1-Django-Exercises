from django.shortcuts import render

def home_view(request):
    return render(request, "hello/home.html")

def about_view(request):
    return render(request, "hello/about.html")