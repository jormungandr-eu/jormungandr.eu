from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.shortcuts import redirect
from django.utils import timezone


def error_404(request):
    """404 page"""

    """Template loading"""
    template = loader.get_template("404.html")

    return HttpResponse(template.render())


def index(request):
    """Index page"""

    """Template loading"""
    template = loader.get_template("jormungandr_index.html")

    """Computed HTML response"""
    return HttpResponse(template.render())


def neige_outside(request, list_min=0, list_max=4):
    """The blog part"""

    """Template loading"""
    template = loader.get_template("neige_outside/index.html")

    """Template filling"""
    next_min = int(list_min) - 4;
    next_max = int(list_max) + 4;
    print "next_min:" + str(next_min)
    print "next_max:" + str(next_max)
    latest_posts = Post.objects.order_by("-pub_date")[list_min:list_max]
    context = RequestContext(request, {
        "latest_posts": latest_posts,
        "is_auth": request.user.is_authenticated(),
        "min": int(list_min),
        "max": int(list_max),
        "next_min": next_min,
        "next_max": next_max,
        "list_index": len(Post.objects.order_by("-pub_date")[:list_max]),
        "list_size": len(Post.objects.order_by("-pub_date")), })

    """Computed HTML response"""
    return HttpResponse(template.render(context))


def posts(request, post_id):
    """Blogs's individual posts"""

    """Template loading"""
    template = loader.get_template("neige_outside/post.html")

    """Template filling"""
    post = Post.objects.filter(id=post_id)
    if post:
        context = RequestContext(request, {
            "post": post[0],
            "is_auth": request.user.is_authenticated(), })
    else:
        return error_404(request)

    return HttpResponse(template.render(context))


def new(request):
    """New post page"""

    if not request.user.is_authenticated():
        return redirect("neige_outside.views.login_view")

    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        post = Post(title=title, text=content, preview=content[0:97] + "...", pub_date=timezone.now())
        post.save()
        return redirect("neige_outside.views.neige_outside")

    context = RequestContext(request, {
        "is_auth": request.user.is_authenticated(), })

    template = loader.get_template("neige_outside/new_post.html")
    return HttpResponse(template.render(context))


def login_view(request):
    """Login page"""

    if request.user.is_authenticated():
        template = loader.get_template("neige_outside/logged_in.html")
        return HttpResponse(template.render())

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("neige_outside.views.neige_outside")

    c = {}
    c.update(csrf(request))
    return render_to_response("neige_outside/login_view.html", c)


def logout_view(request):
    """Logout"""

    logout(request)
    return redirect("neige_outside.views.neige_outside")

