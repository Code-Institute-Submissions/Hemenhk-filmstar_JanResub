from .models import Comment, Contact
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


"""
Note that the Contact code was borrowed from twilio.com's tutorial
"""


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'