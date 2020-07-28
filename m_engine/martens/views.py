# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost


# Create your views here.


def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'martens/main_page.html', context={'posts': posts})



def post_detail(request, slug):
    post = BlogPost.objects.get(slug__iexact=slug)

    return render(request, 'martens/post_detail.html', context={'post': post})
