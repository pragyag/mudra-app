from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from .models import Mudra

# Create your views here.
def index(request):
    mudra_list = Mudra.objects.all()
    template = loader.get_template('mudras/index.html')
    context = RequestContext(request, {
        'mudra_list': mudra_list,
    })
    return HttpResponse(template.render(context))

def detail(request, mudra_id):
    mudra_details = Mudra.objects.get(id=mudra_id)
    template = loader.get_template('mudras/details.html')
    context = RequestContext(request, {
        'mudra_details': mudra_details,
    })
    return HttpResponse(template.render(context))
