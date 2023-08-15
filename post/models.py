from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
import uuid
from djinsta.models import Profile
from notifications.signals import notify


# Create your models here.

def get_profile_url(instance,filename):
    return f'user_{instance.id}/{filename}'

class Tag(models.Model):
	title = models.CharField(max_length=75, verbose_name='Tag')
	slug = models.SlugField(null=False, unique=True)

	class Meta:
		verbose_name='Tag'
		verbose_name_plural = 'Tags'

	def get_absolute_url(self):
		return reverse('tags', args=[self.slug])

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	picture=models.ImageField(upload_to=get_profile_url,verbose_name='Picture',null=True)
	caption = models.TextField(max_length=1500, verbose_name='Caption')
	posted = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)


	def get_absolute_url(self):
		return reverse('postdetails', args=[str(self.id)])

	def __str__(self):
		return str(self.id)


class Follow(models.Model):
	follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='follower')
	following = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='following')
	
@receiver(post_save, sender=Follow)
def add_followed_posts_to_stream(sender, instance, created, **kwargs):
	if created:
		follower = instance.follower
		following = instance.following
		followed_posts = Post.objects.filter(user=following)
		for post in followed_posts:
			Stream.objects.create(
				post=post,
				user=follower,
				following=following,
				date=post.posted,
			)

class Request(models.Model):
    pass


class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)

    def add_post(sender,instance,*args,**kwargs):
        post=instance
        user=post.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream=Stream.objects.create(post=post,user=follower.follower,following=user,date=post.posted)
            stream.save()
            notify.send(user, recipient=follower.follower, verb='Post Notification', description='Just Posted!')
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    posted = models.DateTimeField(auto_now_add=True)




post_save.connect(Stream.add_post, sender=Post)
# post_save.connect(Stream.add_post, sender=Follow)







