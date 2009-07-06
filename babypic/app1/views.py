# -*- coding:utf8 -*-
# Create your views here.
from models import Picture
from django.shortcuts import render_to_response
def index(request):
    return render_to_response('index.html',locals())
def test(request):
    testpic = Picture.objects.filter(type=1)
    return render_to_response('advanced.html',locals())
def aboutus(request):
    return render_to_response('about.html',locals())
    
    
