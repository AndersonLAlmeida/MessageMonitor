from django import forms
from .models import MessageSended, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser

class MessageSendedForm(forms.ModelForm):
    class Meta:
        model = MessageSended
        fields = ['data', 'codigo', 'tipo']