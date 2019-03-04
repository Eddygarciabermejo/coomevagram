""" Users views """
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from users.forms import ProfileForm, SignupForm
from users.models import Profile


def login_view(request):
    """
    Receive username and password to enter the feed template.
    :param request:
    :return: feed or login template.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """
    Close a user's session.
    :param request:
    :return: login view.
    """
    logout(request)

    return redirect('login')


def signup_view(request):
    """
    Create a user register associated with your profile.
    :param request: form fields
    :return: feed template or signup template with error.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form
    }

    return render(request=request, template_name='users/signup.html', context=context)


@login_required
def update_profile(request):
    """
    Call the template to update a user's profile.
    :param request:
    :return: update_profile template.
    """
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.picture = data['picture']
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.save()

            messages.success(request, 'Profile updated correctly')
            return redirect('update_profile')
    else:
        form = ProfileForm()

    context = {
        'profile': profile,
        'user': request.user,
        'form': form
    }

    return render(request=request, template_name='users/update_profile.html', context=context)
