from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    if request.method == "GET":
        return render(request, 'home/index.html')

def register(request):
    if request.method == "GET":
        return render(request, 'home/register.html')
