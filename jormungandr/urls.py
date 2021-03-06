"""jormungandr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url

from neige_outside import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^neige-outside/new/$', views.new),
    url(r'^neige-outside/delete/$', views.delete),
    url(r'^neige-outside/delete/(?P<post_id>[0-9]+)/$', views.delete_view),
    url(r'^neige-outside/$', views.neige_outside),
    url(r'^neige-outside/(?P<post_id>[0-9]+)/$', views.posts),
    url(r'^neige-outside/(?P<list_min>[0-9]+)-(?P<list_max>[0-9]+)/$', views.neige_outside),
    url(r'^neige-outside/login/$', views.login_view),
    url(r'^neige-outside/logout/$', views.logout_view),
]
