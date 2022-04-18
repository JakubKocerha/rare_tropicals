""" import post model to add/edit and display posts"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post


def blog(request):
    """ BLog page to display all available posts """

    posts = Post.objects.all()  # pylint: disable=no-member
    post_count = len(posts)
    template = 'blog/blog.html'
    context = {
        'posts': posts,
        'post_count': post_count
    }
    return render(request, template, context)
