from django import forms
from .models import DirectMessage
from django.forms import ModelForm, Textarea

class ComposeForm(forms.ModelForm):
    class Meta:
        model = DirectMessage
        fields = ('receiver', 'subject', 'body',)
        widgets = {
            'body': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = DirectMessage
        fields = ('body',)
        widgets = {
            'body': Textarea(attrs={'cols': 80, 'rows': 20}),
        }