
from django import template
from djinsta.models import Profile
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