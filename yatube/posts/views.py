from django.shortcuts import render
from .models import Post


# Перевести после проверки


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request):
    template = "posts/group_list.html"
    title = 'Лев Толстой – зеркало русской революции.'
    context = {
        'title': title,
        'text': "Здесь будет информация о группах проекта Yatube",
    }
    return render(request, template, context)
