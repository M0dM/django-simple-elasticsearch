from django import forms
from .models import Blog, BlogPost


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['name', 'description']


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['blog', 'title', 'body']
