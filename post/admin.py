from django.contrib import admin
from.models import Post,Follow,Stream,Tag,Comment,LikeLogs
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(LikeLogs)
admin.site.register(Comment)
# Register your models here.
