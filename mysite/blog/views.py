from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Blog, Comment

def home(request):
	blogs = []
	for i in range(3):
		blogs.append(Blog.objects.order_by('-posted')[i])
	context = {'blogs': blogs}
	return render(request, 'blog/home.html', context)

def about(request):
	context = {}
	return render(request, 'blog/about.html', context)

def tips(request):
	context = {}
	return render(request, 'blog/tips.html', context)

def archive(request):
	blogs = Blog.objects.order_by('-posted')
	context = {'blogs': blogs}
	return render(request, 'blog/archive.html', context)

def entry(request):
	context = {}
	return render(request, 'blog/entry.html', context)
