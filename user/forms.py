from .models import Music
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User





from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Music

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)









from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Music

class MusicUploadForm(forms.ModelForm):
    # email_addresses = forms.CharField(label='Email Addresses', required=False, widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = Music
        fields = ('title', 'artist', 'audio_file',"is_public")

    