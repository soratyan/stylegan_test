from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    if 'name' in request.GET:
        name = request.GET['name']
        result = 'my name is ' + name + '!!'
    else:
        result = 'please input query name'
    return HttpResponse(result)

class IndexTemplateView(TemplateView):
    template_name = "index.html"
