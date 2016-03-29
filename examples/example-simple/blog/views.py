from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from .forms import BlogForm, BlogPostForm
from .models import Blog, BlogPost


def index(request):
    blogs = Blog.objects.all()
    posts = BlogPost.objects.all()
    context = {
        'blogs': blogs,
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


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


def remove_blog(request, _id):
    blog = Blog.objects.filter(pk=_id).get()
    blog.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        _('SUCCESS, blog removed.')
    )
    return redirect('blog:index')


def remove_post(request, _id):
    post = BlogPost.objects.filter(pk=_id).get()
    post.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        _('SUCCESS, post removed.')
    )
    return redirect('blog:index')
