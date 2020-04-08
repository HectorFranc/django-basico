# Django
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView

# Forms
from users.forms import SignupForm

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile


# Create your views here.
class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    slug_url_kwarg = 'username'
    slug_field = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
    login_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


class SignupFormView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def get_context_object(self, **kwargs):
        context = super().get_context_object(kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']
    login_url = reverse_lazy('users:login')

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})
