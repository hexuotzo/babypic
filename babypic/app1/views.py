# -*- coding:utf8 -*-
# Create your views here.

from models import Picture
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _


def index(request):
    return render_to_response('index.html',locals())
def test(request):
    testpic = Picture.objects.filter(type=1)
    return render_to_response('advanced.html',locals())
def aboutus(request):
    return render_to_response('about.html',locals())
    
def i18n(request):
    ab = "About us"
    ga = "Galleries"
    ous = "OurStudio"
    cts = "Contact"
    output = _("Welcome to my site.")
    return render_to_response('base.html',locals())

