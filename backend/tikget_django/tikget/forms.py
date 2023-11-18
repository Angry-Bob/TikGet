from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize field labels or widgets if needed
        self.fields['username'].label = 'Your Username'
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

    def clean_remember_me(self):
        remember_me = self.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)  # Session will expire when the browser is closed
        return remember_me