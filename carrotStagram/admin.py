from django.contrib import admin
from carrotStagram.models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(CommentLikes)
