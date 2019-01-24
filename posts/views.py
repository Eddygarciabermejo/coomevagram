""" Posts views """

from django.http import HttpResponse

from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thepianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
    }
]


def list_posts(request):
    """
    List existing posts with images.
    :param request:
    :return: content html
    """
    content = []

    for post in posts:
        content.append("""
            <p><strong>{name}</stong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))

    # Por cada iteración se concatenará un <br>.
    return HttpResponse('<br>'.join(content))
