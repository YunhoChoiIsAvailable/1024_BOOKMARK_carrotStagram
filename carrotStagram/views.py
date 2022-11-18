from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import *
from carrotStagram.models import *
from django.contrib import auth

# Create your views here.
def loginView(request):
    if request.method == 'GET':
        return render(request, 'carrotStagram/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('userpw', None)

    print(username, password)
    error_message = {}
    if not (username and password):
        error_message['error'] = "올바르지 않은 id/pw입니다"
    else:
        try:
            account = Account.objects.get(name=username)
            if password == account.password:
                request.session['user'] = account.id
                return HttpResponseRedirect(reverse('carrotstagram:friend'))
            else:
                error_message['error']='올바르지 않은 id/pw입니다'
        except:
            error_message['error']='올바르지 않은 id/pw입니다'
    return render(request,'carrotStagram/login.html', error_message)

def settingView(request):
    id = request.session['user']


class FriendView(TemplateView):
    template_name = 'carrotStagram/friend.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.session['user']
        account = Account.objects.get(pk=id)
        posts = []
        for follow_account in account.follows.all():
            for post in follow_account.post_set.all():
                posts.append(post)
        posts = sorted(posts, key = (lambda post : post.modified_dt))
        print(posts)
        context['posts'] = posts
        return context

class FeedView(TemplateView):
    template_name = 'carrotStagram/feed.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.session['user']
        account = Account.objects.get(pk=id)
        posts = Post.objects.all()
        posts = sorted(posts, key=(lambda post: post.modified_dt))
        print(posts)
        context['posts'] = posts
        context['account'] = account
        return context

class MyPageView(DetailView):
    pass

class PostDetailView(DetailView):
    pass

class FollowingView(ListView):
    pass

class FollowerView(ListView):
    pass


