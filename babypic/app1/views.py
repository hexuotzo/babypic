# -*- coding:utf8 -*-
# Create your views here.
from models import Picture,Music,Picstyle
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import Bbs,BbsForm
from django.http import HttpResponse,HttpResponseRedirect
def t(request,tid):
    picstyle = Picstyle.objects.get(id=tid)
    pic = Picture.objects.filter(type=tid)
    return render_to_response('zhuanti.html',locals())
def bbs(request):
    if request.method == 'POST':
        form = BbsForm(request.POST,auto_id=True)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bbs/')
        return render_to_response('bbs.html',locals())
    form = BbsForm()
    content_list = Bbs.objects.order_by('-id')
    paginator = Paginator(content_list,5)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError :
        page = 1

    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('bbs.html',locals())

#def music(request):
#    musiclist = Music.objects.order_by('id')
#    return render_to_response('1234.html',locals())
#def appreciation(request):
#    return render_to_response('appr.html',locals())

def message(request):
    content_list = Bbs.objects.order_by('-id')
    paginator = Paginator(content_list,5)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError :
        page = 1

    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('message.html',locals())
    
