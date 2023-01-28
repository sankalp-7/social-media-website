from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Profile
# Create your views here.

@login_required(login_url='/signin')
def home(request):
    return render(request,'djinsta/index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('/signin')


        else:
            messages.info(request,'Password not matching')
            return redirect('/signup')
    return render(request,'djinsta/signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('/signin')
    return render(request,'djinsta/signin.html')
@login_required(login_url='/signin')
def logout(request):
    auth.logout(request)
    return redirect('/signin')