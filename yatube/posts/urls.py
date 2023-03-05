# yatube/posts/urls.py (File of urls of the posts app)

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index),
    # Groups pages
    path('group/<slug:slug>/', views.group_posts)

]
