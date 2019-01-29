from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    if request.method == "GET":
        return render(request, 'home/index.html')

def register(request):
    if request.method == "GET":
        return render(request, 'home/register.html')

def login(request):
    if request.method == "GET":
        return render(request, 'home/login.html')

def profile(request):
    if request.method == "GET":
        return render(request, 'home/profile.html')

def post_editing(request):
    if request.method == "GET":
        return render(request, 'home/post_editing.html')