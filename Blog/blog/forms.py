from django import forms
from .models import CreateBlog
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email','password')

class CreateBlogForm(forms.ModelForm):
    class Meta():
        model = CreateBlog
        fields = ('title', 'blog')