from django import forms


class BlogForm(forms.Form):

  class Meta:
    model = Blog


class BlogPostForm(forms.Form):

  class Meta:
    model = BlogPost
