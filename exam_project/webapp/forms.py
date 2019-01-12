from django import forms
from webapp.models import UserInfo, Post


class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = []


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['autor']
