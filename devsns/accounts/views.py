from django.shortcuts import redirect, render
from django.contrib import auth

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