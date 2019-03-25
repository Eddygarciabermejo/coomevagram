""" Users views """
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from posts.models import Post
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view """

    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'users/detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ Add user's posts to context """

        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


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
            return redirect('posts:feed')
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

    return redirect('users:login')


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
            return redirect('users:login')
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
    :return: detail template.
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
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    context = {
        'profile': profile,
        'user': request.user,
        'form': form
    }

    return render(request=request, template_name='users/update_profile.html', context=context)
