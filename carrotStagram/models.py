from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    account_img = models.ImageField(upload_to='profiles_imgs')

class FriendTable(models.Model):
    people1 = models.ForeignKey(Account, on_delete=models.CASCADE)
    people2 = models.ForeignKey(Account, on_delete=models.CASCADE)

class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    uploader = models.ForeignKey(Account, on_delete=models.CASCADE)
    like = models.ManyToManyField(Account)
    post_img = models.ImageField(upload_to='post_imgs')

