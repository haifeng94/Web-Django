#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from lh_user import user_decorator
from lh_cart.models import *

@user_decorator.login
def cart(request):
    uid=request.session['user_id']
    carts=CartInfo.objects.filter(user_id=uid)
    context={'title':'购物车',
             'page_name':1,
             'carts':carts}
    return render(request,'lh_cart/cart.html',context)

@user_decorator.login
def add(request,gid,ucount):
    #用户uid购买啦gid商品，数量为ucount
    uid=request.session['user_id']
    gid=int(gid)
    ucount=int(ucount)
    #查询购物车中是否已经有此商品，如果有则数量增加，如果没有则新增
    carts=CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts)>=1:
        cart=carts[0]
        cart.ucount=cart.ucount+ucount
    else:
        cart=CartInfo()
        cart.user_id=uid
        cart.goods_id=gid
        cart.ucount=ucount
    cart.save()
    #如果是ajax请求则返回json,否则转向购物车
    if request.is_ajax():
        ucount=CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'ucount':ucount})
    else:
        return redirect('/cart/')

@user_decorator.login
def edit(request,cart_id,ucount):
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        ucount1=cart.count=int(ucount)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':ucount1}
    return JsonResponse(data)

@user_decorator.login
def delete(request,cart_id):
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)