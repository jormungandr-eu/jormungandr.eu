from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)


def year_archive(request, year="2015"):
    html = "<html><body>Works.</body></html>"
    return HttpResponse(html)


def month_archive(request, year="2015", month="01"):
    html = "<html><body>Works, too.</body></html>"
    return HttpResponse(html)


def article_detail(request, year="2015", month="01", day="01"):
    html = "<html><body>Yup, still works.</body></html>"
    return HttpResponse(html)


def post_view(request, data=""):
    html = "<html><body>%s</body></html>" % data
    return HttpResponse(html)
