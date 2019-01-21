# pylint: disable=no-member
from django.shortcuts import render
from django.http import JsonResponse

from app.models import Users
from hashlib import sha1

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if not all([username, password]):
            return JsonResponse({"code": -1, "info": "请填写用户名或密码"})

        try:
            res = Users.objects.get(username = username)
        except Exception as e:
            res = None
        if res:
            return JsonResponse({"code": -1, "info": "用户名已经存在"})

        # encryption
        sh1 = sha1()
        sh1.update(password.encode('utf-8'))
        pwdd = sh1.hexdigest()
        print(len(pwdd))
        user = Users(username=username, password=pwdd)
        user.save()

        if username == "" or password == "":
            return JsonResponse({"code": -1, "info": "请填写用户名或者密码"})
        else:
            return JsonResponse({"code": 0, "info": ""})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # encryption
        try:
            user = Users.objects.get(username = username)
            sh1 = sha1()
            sh1.update(password.encode('utf-8'))
            pwdd = sh1.hexdigest()
            if user.password == pwdd:
                return JsonResponse({"code": 0, "info": ""})
            else:
                return JsonResponse({"code": -1, "info": "密码错误"}) 
        except:
            return JsonResponse({"code": -1, "info": "用户不存在"}) 