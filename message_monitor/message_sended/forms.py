from django import forms
from .models import MessageSended

class MessageSendedForm(forms.ModelForm):
    class Meta:
        model = MessageSended
        fields = ['data', 'codigo', 'tipo']