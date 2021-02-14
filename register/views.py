from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request, "login.html")



def register(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=password,username=username)
                user.save()
                print('user created')
                return redirect('login')
            # return redirect('/')
        else:
            messages.info(request, "password is not match")
            

    return render(request, "signup.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

