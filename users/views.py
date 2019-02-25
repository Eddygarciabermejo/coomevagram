""" Users views """

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

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
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password does not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        login(request, user)
        return redirect('feed')

    return render(request, 'users/signup.html')


def update_profile(request):
    """
    Call the template to update a user's profile.
    :param request:
    :return: update_profile template.
    """

    profile = request.user.profile

    return render(request=request, template_name='users/update_profile.html', context={'profile': profile, 'user': request.user})
