# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile


# Create your views here.
def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password_confirmation != password:
            return render(request, 'users/signup.html', {'error': 'Passwords does not match'})
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
            except IntegrityError:
                return render(request, 'users/signup.html', {'error': 'Username already taken'})

            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

            profile = Profile(user=user)
            profile.save()

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('feed')

            return redirect('login')
    return render(request, 'users/signup.html')


def update_profile(request):
    return render(request, 'users/update_profile.html')
