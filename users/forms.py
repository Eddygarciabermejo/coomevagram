""" Users forms"""
from django import forms


class ProfileForm(forms.Form):
    """
    Based on the model, the fields that will be used in the form are placed.
    """

    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=True)
