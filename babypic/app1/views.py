# -*- coding:utf8 -*-
# Create your views here.
from models import Picture
from django.shortcuts import render_to_response
def test(request):
    testpic = Picture.objects.get(picname = 'test1')
    return render_to_response('test.html',locals())
    
def testcss(request):
    testpic = Picture.objects.get(picname = 'test1')
    return render_to_response('advanced.html',locals())