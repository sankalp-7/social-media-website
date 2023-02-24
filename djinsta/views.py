from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Profile
from post.models import Follow,Stream
# Create your views here.

@login_required(login_url='/signin')
def home(request):
    posts=Stream.objects.filter(user=request.user)
    users=Profile.objects.all().exclude(user=request.user)
    user_profile_img=Profile.objects.get(user=request.user)
    check_follow_status=Follow.objects.filter(follower=request.user)
    following_list=[]
    for accounts in check_follow_status:
        following_list.append(accounts.following.username)
    return render(request,'djinsta/index.html',{'users':users,'following_list':following_list,'posts':posts,'dp':user_profile_img})

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
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('/settings')


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
@login_required(login_url='/signin')
def settings(request):
    print("settings loading/......")
    curr_user=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES['image']==None:
            print("default image loaded")
            curr_user.profile_img=curr_user.profile_img
            curr_user.bio=request.POST['bio']
            curr_user.location=request.POST['location']
            bool=request.POST['checkprivacy']
            if bool=="0":
                curr_user.account_visibility=False
            else:
                curr_user.account_visibility=True
            curr_user.save()
        else:
            print("personal image dp")
            curr_user.profile_img=request.FILES['image']
            print(curr_user.profile_img)
            curr_user.bio=request.POST['bio']
            curr_user.location=request.POST['location']
            bool=request.POST['checkprivacy']
            if bool=="0":
                curr_user.account_visibility=False
            else:
                curr_user.account_visibility=True
            curr_user.save()
        return redirect('/')
    else:


        return render(request,'djinsta/setting.html',{'user_profile':curr_user})

@login_required(login_url='/signin')
def profile(request):
    curr_user=Profile.objects.get(user=request.user)
    return render(request,'djinsta/profile.html',{'curr_user':curr_user})
@login_required(login_url='/signin')
def follow(request,pk):
    follower=request.user
    following=Profile.objects.get(id_user=pk)
    following.followers+=1
    following.save()
    print(following.user,following.followers)
    follow_obj=Follow.objects.create(follower=follower,following=following.user)
    follow_obj.save()
    return redirect('/')
@login_required(login_url='/signin')
def unfollow(request,pk):
    follower=request.user
    following=Profile.objects.get(id_user=pk)

    if following.followers==0:
        following.followers=0
    else:
        following.followers-=1
    following.save()

    inst=Follow.objects.get(follower=follower,following=following.user)
    inst.delete()
    return redirect('/')
def like_post(request,pid):
    pass
