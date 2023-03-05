from django.shortcuts import render
from django.http import HttpResponse

# Перевести после проверки


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse('Группа {}.'.format(slug))
