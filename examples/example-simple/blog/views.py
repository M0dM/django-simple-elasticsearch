from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from .forms import BlogForm, BlogPostForm


def index(request):
    return render(request, 'blog/index.html')


def add_blog(request):
    form = BlogForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            _('SUCCESS, blog saved.')
        )
        return redirect('blog:index')
    else:
        context = {
            'form': form,
        }
        return render(request, 'blog/add_blog.html', context)


def add_post(request):
    form = BlogPostForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            _('SUCCESS, post saved.')
        )
        return redirect('blog:index')
    else:
        context = {
            'form': form,
        }
        return render(request, 'blog/add_post.html', context)
