""" Users forms """
from django import forms


class ProfileForm(forms.Form):
    """
    The fields are the names defined in the template manually and will be stored in the model.
    """

    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=True)
