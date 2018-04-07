from django.db import models

class CartInfo(models.Model):
    user=models.ForeignKey('lh_user.UserInfo')
    goods=models.ForeignKey('lh_goods.GoodsInfo')
    ucount=models.IntegerField()