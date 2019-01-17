""" Platzigram URLs module """

from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current-server-time/', views.current_server_time),
    path('order-numbers/', views.order_numbers),
    path('hi/<str:name>/<int:age>/', views.say_hi),
]
