from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    follows = models.ManyToManyField('self', blank = True, symmetrical=False, related_name='followers')
    password = models.CharField(max_length=50, blank = False, default='0000')

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField(max_length=200, blank = True)
    uploader = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add = True)
    modified_dt = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    people = models.ManyToManyField(Account)

    def __str__(self):
        return str(self.post) + ' : ' + str(self.count)

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    person = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return str(self.person) + ' -> ' + str(self.post)

class CommentLikes(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    people = models.ManyToManyField(Account)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.comment) + ' : ' + str(self.count)
