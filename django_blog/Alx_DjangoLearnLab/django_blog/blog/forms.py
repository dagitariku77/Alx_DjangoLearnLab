# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from taggit.forms import TagField

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    class PostForm(forms.ModelForm):
           class Meta:
            model = Post
            fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']





        # blog/forms.py


class PostForm(forms.ModelForm):
    tags = TagField() # Use TagField for tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

