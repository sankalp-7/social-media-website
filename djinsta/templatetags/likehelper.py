# likehelper.py
from django import template
from post.models import LikeLogs, Post
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def is_liked(post_id, user_id):
    try:
        post_obj = Post.objects.get(id=post_id)
        user_obj = User.objects.get(id=user_id)
        is_like = LikeLogs.objects.filter(user=user_obj, post=post_obj).exists()
        return is_like
    except (Post.DoesNotExist, User.DoesNotExist):
        return False
