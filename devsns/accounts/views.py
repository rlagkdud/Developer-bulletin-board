from atexit import register
import django
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(req):
    if req.method == "POST":
        username= req.POST['username']
        password = req.POST['password']
        user= auth.authenticate(req,username = username, password = password)

        if user is not None:
            auth.login(req,user);
            return redirect('home')
        else:
            return render(req,'bad_login.html')
    else:
        return render(req, 'login.html')

def logout(req):
    auth.logout(req)
    return redirect('home')

def signup(req):
    if req.method == "POST":
        if req.POST['password'] == req.POST['repeat']:
            #회원가입
            new_user = User.objects.create_user(username =req.POST['username'],password = req.POST['password'])
            #로그인
            auth.login(req, new_user)
            #홈 리다이렉션  
            return redirect('home')
    
    return render(req,'register.html')