from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignupForm
from .models import UserDetail


@require_http_methods(["GET"])
def signout(request):
    """
    This controller is responsible
    to log out user
    """
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return redirect('home')
    

@require_http_methods(["GET"])
def sigin(request):
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
        return redirect('home')
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
        
        try:
            user = User.objects.create_user(
            form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
        except:
            messages.error(request, 'Your email is already taken')
            return redirect('/signup')
        
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        detail = UserDetail()
        detail.first_name = form.cleaned_data['first_name']
        detail.last_name = form.cleaned_data['last_name']
        detail.gender = form.cleaned_data['gender']
        detail.phone = '+62' + form.cleaned_data['phone']
        detail.identifier = form.cleaned_data['identifier']
        detail.address = form.cleaned_data['address']
        detail.provience = form.cleaned_data['province']
        detail.city = form.cleaned_data['city']
        detail.zipcode = form.cleaned_data['zipcode']
        detail.user = user
        detail.save()

        return redirect('/login')
    return render('/register')
