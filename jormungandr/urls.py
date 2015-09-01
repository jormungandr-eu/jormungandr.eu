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
    url(r'^neige-outside/$', views.home),
    url(r'^neige-outside/([0-9]{4})/$', views.year_archive),
    url(r'^neige-outside/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^neige-outside/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    url(r'^neige-outside/post/([a-zA-Z0-9_.-]+)/$', views.post_view),
]
