#coding=utf-8
from django.shortcuts import render,redirect
from lh_user.models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect

def register(request):
    return render(request,'lh_user/register.html')

def register_handle(request):
    #接受用户输入
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    upwd2=post.get('cpwd')
    uemail=post.get('email')

    #判断两次密码输入
    if upwd != upwd2:
        return redirect('/user/register')

    #python默认下为unicode，python3需要encode成utf-8
    upwd=upwd.encode('utf-8')

    #密码加密
    s1=sha1()
    s1.update(upwd)
    upwd3=s1.hexdigest()

    #创建对象
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail=uemail

    #存放到数据库中去
    user.save()

    #注册成功，转到登录页面
    return redirect('/user/login')

def register_exist(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'lh_user/login.html',context)

def login_handle(request):
    #接受请求信息
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    jizhu=post.get('jizhu',0)
    #根据用户名查询对象
    users=UserInfo.objects.filter(uname=uname)#[]
    print (uname)
    #判断：如果未查到则用户名报错，如果查到则判断密码是否正确，正确则转到用户中心
    if len(users)==1:
        upwd = upwd.encode('utf-8')
        s1=sha1()
        s1.update(upwd)
        if s1.hexdigest()==users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            #记住用户名
            if jizhu!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname,'upwd':upwd}
            return render(request,'lh_user/login.html',context)

def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
    context={
        'title':'用户中心',
        'user_email':user_email,
        'user_name':request.session['user_name']
    }
    return render(request,'lh_user/user_center_info.html',context)

def order(request):
    context={'title':'用户中心'}
    return render(request,'lh_user/user_center_order.html',context)

def site(request):
    user=UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post=request.POST
        user.ushou=post.get('ushou')
        user.uaddress=post.get('uaddress')
        user.uyoubian=post.get('uyoubian')
        user.uphone=post.get('uphone')
        user.save()
    context={'title':'用户中心','user':user}
    return render(request,'lh_user/user_center_site.html',context)


