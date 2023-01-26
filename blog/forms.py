from .models import Comment, Contact, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('likes',)
        widgets = {
            'content': SummernoteWidget(),
        }


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
