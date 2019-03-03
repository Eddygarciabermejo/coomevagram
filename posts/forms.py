""" Posts forms """
from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    """
    The model's fields that will be used to create the form are placed.
    """
    class Meta:
        """ Form settings """
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
