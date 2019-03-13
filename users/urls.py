""" Users URLs """

from django.urls import path
from users import views

urlpatterns = [
    path(route='login/', view=views.login_view, name="login"),
    path(route='logout/', view=views.logout_view, name="logout"),
    path(route='signup/', view=views.signup_view, name="signup"),
    path(route='me/profile', view=views.update_profile, name="update_profile"),
]
