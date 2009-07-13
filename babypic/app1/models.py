# -*- coding:utf8 -*-
import os
from django.db import models
from settings import MEDIA_ROOT
from django.utils.translation import ugettext as _
from django.db.models.fields.files import ImageFieldFile
from utils import make_thumb,make_thumb_small

UPLOAD_ROOT = 'item'
THUMB_ROOT = 'thumb'
THUMB_SMALL_ROOT = 'thumb/small'
class Picstyle(models.Model):
    style = models.CharField('风格',max_length=50)
    def __unicode__(self):
        return self.style
class Picture(models.Model):
    picname = models.CharField('图片名称',max_length=80,blank = True ,help_text='（非必填）')
    #describe = models.CharField('相片描述',max_length=200,help_text='照片的注释，会显示在相片下面')
    pic = models.ImageField('图片上传',upload_to = UPLOAD_ROOT )
    thumb = models.ImageField(upload_to = THUMB_ROOT, blank = True,
           help_text='预览图 ， 系统会自动生成， 也可以自己上传（非必填）')
    thumb_small = models.ImageField(upload_to = THUMB_SMALL_ROOT, blank = True,
           help_text='缩略图 ， 系统会自动生成， 也可以自己上传（非必填）')
    type = models.ForeignKey(Picstyle,verbose_name = '照片位置',help_text='图片会自动上传到您指定的相册位置')
    class Meta:
        verbose_name_plural = _('Picture')
    def save(self):
        base, ext = os.path.splitext(os.path.basename(self.pic.path))
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.pic.name))
        thumb_pixbuf_small = make_thumb_small(os.path.join(MEDIA_ROOT, self.pic.name))
        relate_thumb_path = os.path.join(THUMB_ROOT, base + '_thumb' + ext)
        relate_thumb_small_path = os.path.join(THUMB_SMALL_ROOT, base + '_thumb' + ext)
        thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path)
        thumb_small_path = os.path.join(MEDIA_ROOT, relate_thumb_small_path)
        thumb_pixbuf.save(thumb_path)
        thumb_pixbuf_small.save(thumb_small_path)
        self.thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
        self.thumb_small = ImageFieldFile(self,self.thumb_small,relate_thumb_small_path)
        super(Picture, self).save()


    def __unicode__(self):
        return '%s -- in %s' %(self.picname,self.type)