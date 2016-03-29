import pytest
from django.core.urlresolvers import reverse
from pyquery import PyQuery as pq

pytestmark = pytest.mark.django_db


def test_index_get(client):
    response = client.get(reverse('blog:index'))
    assert response.status_code == 200
    html = pq(response.content)
    link_add_blog = html('a[href="' + reverse('blog:add_blog') + '"]')
    link_add_post = html('a[href="' + reverse('blog:add_post') + '"]')
    assert link_add_blog
    assert link_add_post


def test_add_blog_get(client):
    response = client.get(reverse('blog:add_blog'))
    assert response.status_code == 200
    html = pq(response.content)
    form = html('form[action="' + reverse('blog:add_blog') + '"]')
    assert form


def test_add_blogpost_get(client):
    response = client.get(reverse('blog:add_post'))
    assert response.status_code == 200
    html = pq(response.content)
    form = html('form[action="' + reverse('blog:add_post') + '"]')
    assert form


def test_add_blog_post(client):
    response = client.post(
        reverse('blog:add_blog'),
        {
            'name': "Test blog",
            'description': "Blog description",
        }
    )
    assert response.status_code == 302
    assert response['Location'] == reverse('blog:index')


def test_add_blogpost_post(client, blog):
    response = client.post(
        reverse('blog:add_post'),
        {
            'blog': blog.id,
            'title': "Test post",
            'body': "Post body",
        }
    )
    assert response.status_code == 302
    assert response['Location'] == reverse('blog:index')
