# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


# Create your views here.
@login_required
def list_posts(request):
    """List existing posts"""
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})
