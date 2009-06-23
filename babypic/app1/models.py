# -*- coding:utf8 -*-
from django.db import models
# Create your models here.
UPLOAD_ROOT = 'item'

class Picstyle(models.Model):
    style = models.CharField('风格',max_length=50)
    def __unicode__(self):
        return self.style
class Albums(models.Model):
    typename = models.CharField('相册名',max_length=50)
    describe = models.TextField('相册介绍',help_text = '对相册内容的介绍， 此段文字会显示在相册下面')
    type = models.ForeignKey(Picstyle,verbose_name = '摄影风格')
    def __unicode__(self):
        return self.typename
class Picture(models.Model):
    picname = models.CharField('图片名称',max_length=80)
    describe = models.CharField('相片描述',max_length=200,help_text='照片的注释，会显示在相片下面')
    pic = models.ImageField('选择一张图片',upload_to = UPLOAD_ROOT )
    type = models.ForeignKey(Albums,verbose_name = '相册选择',help_text='图片会自动上传到您指定的相册位置')
    def __unicode__(self):
        return '%s -- in %s' %(self.picname,self.type)
