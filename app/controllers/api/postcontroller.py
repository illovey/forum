# pylint: disable=no-member
from app.models import Users
from hashlib import sha1
from app.models import Posts
from django.http import JsonResponse
import operator
import json
from django.core import serializers

import time

def post_editing(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
    
    if not all([title, content]):
            return JsonResponse({"code": -1, "info": "请填写标题和内容"})

    create_time = int(time.time())
    username = request.session.get('username', '')

    post = Posts(title = title, content = content, create_time = create_time, username = username)
    post.save()
    return JsonResponse({"code": 0, "info": ""})

def getuserposts(request):
    username = request.session.get('username', '')
    postsQuerySet = Posts.objects.filter(username=username)

    result = serializers.serialize('json', list(postsQuerySet))
    return JsonResponse({"code": 0, "info": "", "body": result})

