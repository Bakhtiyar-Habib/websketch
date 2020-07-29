from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def services_view(request, *args, **kwargs):
	return render(request, "services.html", {})

def form_view(request, *args, **kwargs):
	return render(request, "form.html", {})

def blog_view(request, *args, **kwargs):
	return render(request, "blog.html", {})

def webdev_view(request, *args, **kwargs):
	return render(request, "webdev.html", {})

def mobileapp_view(request, *args, **kwargs):
	return render(request, "mobileapp.html", {})

def whyus_view(request, *args, **kwargs):
	return render(request, "whyus.html", {})