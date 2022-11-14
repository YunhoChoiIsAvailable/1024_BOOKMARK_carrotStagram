from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    account_img = models.ImageField(upload_to='profiles_imgs')
    follow_set = models.ManyToManyField('self', blank = True)
    following_set = models.ManyToManyField('self', blank = True)
    password = models.CharField(max_length=50)


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField(max_length=200)
    uploader = models.ForeignKey(Account, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='post_imgs')
    created_dt = models.DateTimeField(auto_now_add = True)
    modified_dt = models.DateTimeField(auto_now = True)

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    count = models.IntegerField(max_length=10)
    people = models.ManyToManyField(Account, on_delete=models.CASCADE)

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    person = models.ManyToManyField(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

class CommentLikes(models.Model):
    comment = models. ForeignKey(Comments, on_delete=models.CASCADE)
    people = models.ManyToManyField(Account, on_delete=models.CASCADE)
    count = models.IntegerField(max_length=10)

