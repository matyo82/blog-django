from django import forms
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'comment-name', 'placeholder': 'Your name', 'aria-label': 'Input for your name'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'ml-5', 'id': 'comment-email', 'placeholder': 'Your email', 'aria-label': 'Input for email'}))
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'id': 'comment-message', 'placeholder': 'Write a message', 'rows': 5,
               'aria-label': 'Input for writing message'}))
