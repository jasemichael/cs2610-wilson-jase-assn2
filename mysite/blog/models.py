from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	content = models.TextField()
	posted = models.DateTimeField()
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE,)
	commenter = models.CharField(max_length=200)
	email = models.EmailField()
	content = models.TextField()
	posted = models.DateTimeField()	
	
	def __str__(self):
		return self.content
