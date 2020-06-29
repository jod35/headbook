# from models import Post
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

# The User CReation form


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2')


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
