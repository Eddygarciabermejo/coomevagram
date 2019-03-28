""" Users forms """
from django import forms
from django.contrib.auth.models import User

from users.models import Profile


class ProfileForm(forms.ModelForm):
    """
    The fields are the names defined in the template manually and will be stored in the model.
    """
    
    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=True)

    class Meta:
        model = Profile
        fields = ['website', 'biography', 'phone_number', 'picture']


class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length=100, widget=forms.EmailInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control', 'placeholder': self.snake_to_word(f)})

    @staticmethod
    def snake_to_word(word):
        """ Change snake case to word """
        return ' '.join(x.capitalize() or '_' for x in word.split('_'))

    def clean_username(self):
        """ Username must be unique """
        username = self.cleaned_data['username']

        username_taken = User.objects.all().filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """ Verify password confirmation match """
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data

    def save(self):
        """ Create user and profile """
        data = self.cleaned_data
        # Elimina el campo del listado ya que no se tendrá en cuenta para ser almacenado.
        data.pop('password_confirmation')

        # Para no asignar 1 a 1 los valores, con **data será suficiente.
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
