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
    page = request.GET['page']
    if not page:
        page = 1
    
    username = request.session.get('username', '')
    total = Posts.objects.filter(username=username).count()
    start = (int(page) - 1) * 3

    postsQuerySet = Posts.objects.filter(username=username)[start:start + 3]
    for postQuerySet in postsQuerySet:
        postQuerySet.content = postQuerySet.content[0:50] + "..."

    posts = serializers.serialize('json', list(postsQuerySet))

    return JsonResponse({"code": 0, "info": "", "body": {'posts': posts, 'total': total}})

def post_details(request):
    if request.method == "POST":
        post_id = request.POST['post_id']
    postsQuerySet = Posts.objects.filter(id = post_id)    
    result = serializers.serialize('json', list(postsQuerySet))
    return JsonResponse({"code": 0, "info": "", "body": result})
