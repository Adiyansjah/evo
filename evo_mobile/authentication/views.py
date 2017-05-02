from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import SignupForm


@require_http_methods(["GET"])
def login(request):
    """
    This controller is responsible
    to render view with login template
    """
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'authentication/login.html')


@require_http_methods(["POST"])
def authentication(request):
    """
    This controller is responsible
    to authenticate user with email and password
    """
    if request.user.is_authenticated:
        return redirect('home')

    username = request.POST.get('email', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('login')
    else:
        messages.error(request, 'Username or Password is incorrect')
        return redirect('login')


@require_http_methods(["GET"])
def register(request):
    """
    This controller is responsible
    to render view with register template
    """
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'authentication/register.html')


@require_http_methods(["POST"])
def create_user(request):
    """
    This controller is responsible
    to handle data from register page
    to create a new user.
    """
    if request.user.is_authenticated:
        return redirect('home')

    form = SignupForm(request.POST.dict())
    if form.is_valid():
        user = User.objects.create_user(
            form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        return redirect('/login')
    return render('/register')
