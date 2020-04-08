# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    template_name = "posts/feed.html"
    model = Post
    ordering = ('-created', )
    paginate_by = 2
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = 'post'


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
