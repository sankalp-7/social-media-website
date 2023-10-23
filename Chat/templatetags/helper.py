import collections
from django import template
from djinsta.models import Profile
from Chat.models import Message
register = template.Library()

@register.filter
def get_profile_img(id):
    profile_obj=Profile.objects.get(id_user=id)
    return profile_obj.profile_img.url
@register.filter
def check_user(users_list):
    if users_list[0]==users_list[1]:
        return 'True'
    return 'False'
@register.filter
def getlastmsg(key):
    dic=collections.defaultdict(list)
    recent_messages=Message.objects.all()
    for m in recent_messages:
        val=f"{m.content}"
        dic[m.room.slug].append(val)
    for k,v in dic.items():
        dic[k]=v[-1]
    if len(dic[key])==0:
        return ""
    return dic[key]
@register.filter
def getusr(key):
    dic=collections.defaultdict(list)
    recent_messages=Message.objects.all()
    for m in recent_messages:
        val=f"{m.user}"
        dic[m.room.slug].append(val)
    for k,v in dic.items():
        dic[k]=v[-1]
    if len(dic[key])==0:
        return ""
    return dic[key]+":"


