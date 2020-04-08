# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    template_name = "posts/feed.html"
    model = Post
    ordering = ('-created', )
    paginate_by = 30
    context_object_name = 'posts'

    login_url = reverse_lazy('users:login')


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    login_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
