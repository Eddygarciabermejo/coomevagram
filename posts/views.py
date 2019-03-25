""" Posts views """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from datetime import datetime

from posts.forms import PostForm
from posts.models import Post

"""
posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036'
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903'
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076'
    }
]
"""


class PostsFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts """

    model = Post
    ordering = ('-created', )
    paginate_by = 2
    template_name = 'posts/feed.html'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """ Post detail view """

    queryset = Post.objects.all()
    template_name = 'posts/detail.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    """ Create a new post """

    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    template_name = 'posts/new.html'

    def get_context_data(self, **kwargs):
        """ Add user and profile to context """

        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
