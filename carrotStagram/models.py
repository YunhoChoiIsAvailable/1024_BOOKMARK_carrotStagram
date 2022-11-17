from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    account_img = models.ImageField(upload_to='profiles_imgs', blank = True)
    follows = models.ManyToManyField('self', blank = True, symmetrical=False, related_name='account_followers')
    password = models.CharField(max_length=50, blank = False, default='0000')


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField(max_length=200, blank = True)
    uploader = models.ForeignKey(Account, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='post_imgs')
    created_dt = models.DateTimeField(auto_now_add = True)
    modified_dt = models.DateTimeField(auto_now = True)

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    count = models.IntegerField()
    people = models.ManyToManyField(Account)

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    person = models.ManyToManyField(Account)
    content = models.CharField(max_length=500)

class CommentLikes(models.Model):
    comment = models. ForeignKey(Comments, on_delete=models.CASCADE)
    people = models.ManyToManyField(Account)
    count = models.IntegerField()
