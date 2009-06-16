# -*- coding:utf8 -*-
# Create your views here.
from models import Picture
from django.shortcuts import render_to_response
def test(request):
    testpic = Picture.objects.get(picname = '萌图')
    return render_to_response('test.html',locals())
    