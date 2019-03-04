""" Posts views """

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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


@login_required
def list_posts(request):
    """
    Send a dictionary of posts to visualize them in the template.
    :param request:
    :return: render to feed template.
    """
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request):
    """
    Create a new post based on the Django Form.
    :param request:
    :return: render to feed template with post created.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    context = {
        'profile': request.user.profile,
        'user': request.user,
        'form': form
    }

    return render(request=request, template_name='posts/new.html', context=context)
