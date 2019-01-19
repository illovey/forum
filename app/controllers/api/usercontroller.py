from django.shortcuts import render
from django.http import JsonResponse

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if username == "" or password == "":
            return JsonResponse({"code": -1, "info": "请填写用户名或者密码"})
        else:
            return JsonResponse({"code": 0, "info": ""})