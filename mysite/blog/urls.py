from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
	path('about/', views.about, name='about'),
 	path('tips/', views.tips, name='tips'),
	path('', views.index, name='index'),

]
