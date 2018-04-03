#coding=utf-8
from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=20)
    gpic=models.ImageField(upload_to='lh_goods')
    gprice=models.DecimalField(max_digits=7,decimal_places=2)
    isDelete=models.BooleanField(default=False)
    gunit=models.CharField(max_length=20,default='人')
    gclick=models.IntegerField()
    gbrief=models.CharField(max_length=300)
    gstock=models.IntegerField()
    gdetails=HTMLField()
    gtype=models.ForeignKey(TypeInfo)