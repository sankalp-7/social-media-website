from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notifications.signals import notify
from.models import Profile
from post.models import Follow,Stream,Post,Comment
from notifications.models import Notification
from itertools import chain
from post.models import LikeLogs

@login_required(login_url='/signin')
def home(request):
    if request.method=='POST' or request.FILES:            #post creation handler
        user_post=request.FILES['user_post']
        caption=request.POST['caption']
        obj=Post.objects.create(picture=user_post,caption=caption,user=request.user)
        print("POST CREATED")
    posts=Stream.objects.filter(user=request.user)         #getting the feed for the current user based on whom he follows
    posts=posts[::-1]                                      #can use ml algorithms here for content recommendation
    users=Profile.objects.all().exclude(user=request.user) 
    try:
        user_profile_img=Profile.objects.get(user=request.user) #getting the profile pic of user, if its not uploaded , take default.png as profile pic
    except:
        user_profile_img='default.png'
    check_follow_status=Follow.objects.filter(follower=request.user)
    following_list=[]
    for accounts in check_follow_status:  #get all those users which the logged in user follows
        following_list.append(accounts.following.username)
    likestatus=LikeLogs.objects.filter(user=request.user)
    return render(request,'djinsta/index.html',{'users':users,'following_list':following_list,'posts':posts,'dp':user_profile_img})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        #form validation with error notification 
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/signup')
            else:
                #user creation
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
    #change user's bio,dp,location
    curr_user=Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES['image']==None:
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
            curr_user.profile_img=request.FILES['image']
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
    notify.send(follower, recipient=following.user, verb='Follow Notification', description='followed you') #send notification to followed user from the followee
    follow_obj=Follow.objects.create(follower=follower,following=following.user)
    follow_obj.save()
    response_data = {'success': True, 'message': 'User followed successfully.','fc':following.followers}
    return JsonResponse(response_data)

@login_required(login_url='/signin')
def unfollow(request, pk):
    follower = request.user
    following = Profile.objects.get(id_user=pk)

    if following.followers > 0:
        following.followers -= 1
        following.save()

        inst = Follow.objects.filter(follower=follower, following=following.user).first()
        if inst:
            inst.delete() #delete follow object==user unfollowed another user

        response_data = {'success': True, 'message': 'User unfollowed successfully.', 'fc': following.followers}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'success': False, 'message': 'User already has 0 followers.', 'fc': following.followers})
    
def like_post(request, pid):
    post_obj = Post.objects.get(id=pid)
    post_obj.likes += 1
    post_obj._meta.auto_created = True
    post_obj.save()
    post_obj._meta.auto_created = False
    likeobj=LikeLogs.objects.create(user=request.user,post=post_obj)
    likeobj.save()
    sender = Profile.objects.get(user=request.user)
    receiver = post_obj.user
    notify.send(sender, recipient=receiver, verb='Like Notification', description='liked your post')

    # Return the updated like count as JSON
    data = {'like_count': post_obj.likes}
    print("\\\\\\\\\\\\\\\\\\")
    print()
    print(data)
    return JsonResponse(data)

def dislike_post(request, pid):
    post_obj = Post.objects.get(id=pid)
    post_obj.likes -= 1
    post_obj._meta.auto_created = True
    post_obj.save()
    post_obj._meta.auto_created = False
    likeobj=LikeLogs.objects.filter(user=request.user,post=post_obj).delete()
    likeobj.save()
    data = {'like_count': post_obj.likes}
    print("\\\\\\\\\\\\\\\\\\")
    print()
    print(data)
    return JsonResponse(data)

def profile(request,pk):
    user=Profile.objects.get(id_user=pk)
    post_count=Post.objects.filter(user=user.user).count()
    following_count=Follow.objects.filter(follower=user.user).count()
    posts=Post.objects.filter(user=user.user)
    return render(request,'djinsta/profile.html',{'user':user,'photos':posts,'post_count':post_count,'following_count':following_count})

def delete_notification(request,pk):
    user=User.objects.get(pk=pk)
    qs=Notification.objects.filter(deleted=False,recipient=user).delete()
    return JsonResponse({'result':'success'})

def comment(request):
    curr_user=Profile.objects.get(user=request.user)
    #comment handler
    if request.method=='POST':
        post_id=request.POST['post_id']
        comment=request.POST['comment']
        post_obj=Post.objects.get(id=post_id)
        comment=Comment.objects.create(post=post_obj,user=curr_user.user,content=comment)
        notify.send(curr_user.user, recipient=post_obj.user, verb='Comment Notification', description='Commented On Your Post') #send comment notification
    data = {
            'post_id':post_id,
            'comment_text': comment.content,
            'comment_user': comment.user.username,
        }
    return JsonResponse(data)

def search_user(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    check_follow_status=Follow.objects.filter(follower=request.user)
    following_list=[]
    for accounts in check_follow_status:
        following_list.append(accounts.following.username)
    if request.method == 'POST':
        username = request.POST['search-username']
        username_object = User.objects.filter(username__icontains=username) #get requested user through username
        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        username_profile_list = list(chain(*username_profile_list))
    
    return render(request, 'djinsta/search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list,'username':username,'following_list':following_list})




