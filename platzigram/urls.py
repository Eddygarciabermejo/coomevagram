""" Platzigram URLs module """

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from platzigram import views as local_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('current-server-time/', local_views.current_server_time, name="server_time"),
    path('order-numbers/', local_views.order_numbers, name="sort"),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name="hi"),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
