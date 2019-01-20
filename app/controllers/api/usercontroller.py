from django.shortcuts import render
from django.http import JsonResponse

from app.models import Users
from hashlib import sha1

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

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