# coding: utf-8
from forum.settings import EXCLUDE_URL
from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
import re
 
exclued_path = [re.compile(item) for item in EXCLUDE_URL]
 
class QtsAuthenticationMiddleware(MiddlewareMixin):
 
    def process_request(self, request):
        url_path = request.path
        for each in exclued_path:
            if re.match(each, url_path):
               return  JsonResponse({"code": 0, "info": ""})
        if request.user.is_authenticated:
            return 
        else:
            return HttpResponseRedirect('/home/login')