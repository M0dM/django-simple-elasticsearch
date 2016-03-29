from django import forms
from .models import Blog, BlogPost


class BlogForm(forms.Form):

    class Meta:
        model = Blog


class BlogPostForm(forms.Form):

    class Meta:
        model = BlogPost
