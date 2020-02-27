from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Blog, Comment
from django.utils import timezone

def home(request):
	blogs = []
	if len(Blog.objects.all()) < 3:
		for blog in Blog.objects.order_by('-posted'):
			blogs.append(blog)	
	else:
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

def entry(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	comments = blog.comment_set.all().order_by('-posted')
	if request.method == "POST":
		comment = blog.comment_set.create(commenter=request.POST['author'], email=request.POST['email'], content=request.POST['content'], posted=timezone.now())
		blog.save()
		return HttpResponseRedirect(reverse('blog:entry', args=[blog_id]))
	else:
		context = {'comments': comments, 'blog':blog}
		return render(request, 'blog/entry.html', context)
