from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.shortcuts import render_to_response
from django.template.context_processors import csrf


csrf_token = {}


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


def new(request):
    """New post page"""

    csrf_token.update(csrf(request))
    if request.user.is_authenticated():
        template = loader.get_template('neige_outside/new_post.html')
        return HttpResponse(template.render())

    return login_view(request)


def login_view(request):
    """Login page"""

    csrf_token.update(csrf(request))

    return render_to_response('neige_outside/login_view.html', csrf_token)


def login(request):
    """Login"""

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return neige_outside(request)

    return HttpResponse("login failed")


def logout_view(request):
    """Logout"""

    logout(request)
    return index(request)

