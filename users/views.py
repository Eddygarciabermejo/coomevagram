""" Users views """
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

from posts.models import Post
from users.forms import SignupForm, ProfileForm
from users.models import Profile


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


class SignupView(FormView):
    """ User sign up view """

    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        """ Save form data """
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """ Login view """

    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    """ Logout view """
    pass


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Update profile view """

    model = Profile
    form_class = ProfileForm
    template_name = 'users/update_profile.html'

    def get_object(self, queryset=None):
        """ Return user's profile """
        return self.request.user.profile

    def get_success_url(self):
        """ Return to user's profile with a form is valid """
        username = self.object.user.username
        return reverse_lazy('users:detail', kwargs={'username': username})
