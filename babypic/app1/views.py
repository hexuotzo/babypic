# -*- coding:utf8 -*-
# Create your views here.
from models import Picture,Music,Picstyle
from django.shortcuts import render_to_response
def index(request):
    return render_to_response('index.html',locals())
def t(request,tid):
    picstyle = Picstyle.objects.get(id=tid)
    pic = Picture.objects.filter(type=tid)
    return render_to_response('zhuanti.html',locals())

#def music(request):
#    musiclist = Music.objects.order_by('id')
#    return render_to_response('1234.html',locals())
#def appreciation(request):
#    return render_to_response('appr.html',locals())


