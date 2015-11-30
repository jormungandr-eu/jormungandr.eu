from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Post


def error_404(request):
    """404 page"""

    """Template loading"""
    template = loader.get_template('404.html')

    return HttpResponse(template.render())


def index(request):
    """Index page"""

    """Template loading"""
    template = loader.get_template('jormungandr_index.html')

    """Computed HTML response"""
    return HttpResponse(template.render())


def neige_outside(request):
    """The blog part"""

    """Template loading"""
    template = loader.get_template('neige_outside/index.html')

    """Template filling"""
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = RequestContext(request, {
        'latest_posts': latest_posts, })

    """Computed HTML response"""
    return HttpResponse(template.render(context))


def posts(request, post_id):
    """Blogs's individual posts"""

    """Template loading"""
    template = loader.get_template('neige_outside/post.html')

    """Template filling"""
    post = Post.objects.filter(id=post_id)
    if post:
        context = RequestContext(request, {
            'post': post[0], })
    else:
        return error_404(request)

    return HttpResponse(template.render(context))
