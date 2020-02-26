from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
	path('about/', views.about, name='about'),
 	path('tips/', views.tips, name='tips'),
	path('home/', views.home, name='home'),
	path('archive/', views.archive, name='archive'),
	path('entry/', views.entry, name='entry'),

]
