from django import forms
from .models import CreateBlog
from django.core import validators
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    # def clean(self):
    #     data = super().clean()
    #     username = data['username']
    #     if User.objects.get(username=username):
    #         raise forms.ValidationError('User Name Already Exists')


class CreateBlogForm(forms.ModelForm):
    class Meta():
        model = CreateBlog
        fields = ('title', 'blog')
