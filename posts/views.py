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


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile,
        }
    )
