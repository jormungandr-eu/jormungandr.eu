from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    """Index page"""
    disp_hello = 1

    """Template loading"""
    template = loader.get_template('neige_outside/index.html')

    """Template filling"""
    context = RequestContext(request, {
        'disp_hello': disp_hello, })

    """Computed HTML response"""
    return HttpResponse(template.render(context))

