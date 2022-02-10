from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

# naming this view specifically 'blog-home' will help us avoid confusions between other urls in our project that might
# be named 'home'