from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import *
from carrotStagram.models import *

def logincheck(f):
    def func(request, *args, **kwargs):
        if 'user' not in request.session.keys():
            return HttpResponseRedirect(reverse('carrotstagram:login'))
        return f(request, *args, **kwargs)
    return func

def get_account_info(request):
    id = request.session['user']
    return Account.objects.get(pk = id)

# Create your views here.
def loginView(request):
    if request.method == 'GET':
        if 'user' in request.session.keys():
            return HttpResponseRedirect(reverse('carrotstagram:friend'))
        return render(request, 'carrotStagram/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('userpw', None)

    print(username, password) # 디버깅용 코드
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

@logincheck
def logout(request):
    del request.session['user']
    return HttpResponseRedirect(reverse('carrotstagram:login'))

@logincheck
def settingView(request):
    id = request.session['user']
    context = {}
    context['account'] = get_account_info(request)
    return render(request, 'carrotStagram/settings.html' , context)

def postnotliked(post, account):
    likes = post.likes_set.all()
    if likes.count() == 0:
        return True
    elif account in likes[0].people.all():
        return False
    return True


def likemodify(like, account):
    '''
    밑에 2개 함수에서 쓰임
    :param like:
    :param account:
    :return:
    '''
    if account in like.people.all():
        like.count -= 1
        like.people.remove(account.pk)
    else:
        like.count += 1
        like.people.add(account.pk)
    return like

@logincheck
def post_like(request, pk):
    account = get_account_info(request)
    post = Post.objects.get(pk=pk)
    likes = post.likes_set.all()
    if likes.count() == 0:
        like = post.likes_set.create(count=0)
        likes = [like]
        like = likemodify(likes[0], account)
    else:
        like = likemodify(likes[0], account)
    like.save()
    return HttpResponseRedirect(request.GET['next'])

@logincheck
def comment_like(request, pk):
    account = get_account_info(request)
    comment = Comments.objects.get(pk = pk)
    likes = comment.commentlikes_set.all()
    if likes.count() == 0:
        like = comment.likes_set.create(count=0)
        likes = [like]
        like = comment.commentlikes_set.add(count=1, people=account.pk)
    else:
        like = likemodify(likes[0], account)
    like.save()
    return HttpResponseRedirect(request.GET['next'])

@logincheck
def comment_add(request):
    if request.method == 'POST':
        pass

class FriendView(TemplateView):
    template_name = 'carrotStagram/friend.html'

    def get(self, request, *args, **kwargs):
        if 'user' not in request.session.keys():
            return HttpResponseRedirect(reverse('carrotstagram:login'))
        ret = super().get(request, *args, **kwargs)
        return ret
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = get_account_info(self.request)
        posts = []
        for follow_account in account.follows.all():
            for post in follow_account.post_set.all():
                post.notliked = postnotliked(post, account)
                posts.append(post)
        posts = sorted(posts, key=(lambda post : post.modified_dt))
        posts = posts[-1::-1]
        context['posts'] = posts
        return context

class FeedView(TemplateView):
    template_name = 'carrotStagram/feed.html'

    def get(self, request, *args, **kwargs):
        if 'user' not in request.session.keys():
            return HttpResponseRedirect(reverse('carrotstagram:login'))
        ret = super().get(request, *args, **kwargs)
        return ret
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.session['user']
        account = Account.objects.get(pk=id)
        posts = Post.objects.all()
        posts = sorted(posts, key=(lambda post: post.modified_dt))
        posts = posts[-1::-1]
        for i in range(len(posts)):
            posts[i].notliked = postnotliked(posts[i], account)
        context['posts'] = posts
        context['account'] = account
        return context

class MyPageView(TemplateView):
    template_name = 'carrotStagram/mypage.html'

    def get(self, request, *args, **kwargs):
        if 'user' not in request.session.keys():
            return HttpResponseRedirect(reverse('carrotstagram:login'))
        ret = super().get(request, *args, **kwargs)
        return ret
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.session['user']
        account = Account.objects.get(pk=id)
        posts = account.post_set.all()
        posts = sorted(posts, key=(lambda post: post.modified_dt))
        posts = posts[-1::-1]
        for i in range(len(posts)):
            posts[i].notliked = postnotliked(posts[i], account)
        context['posts'] = posts
        context['account'] = account
        return context

class PostDetailView(DetailView):
    template_name = 'carrotStagram/postdetails.html'
    model = Post

    def get(self, request, *args, **kwargs):
        if 'user' not in request.session.keys():
            return HttpResponseRedirect(reverse('carrotstagram:login'))
        ret = super().get(request, *args, **kwargs)
        return ret
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = get_account_info(self.request)
        context['account'] = account
        return context

class FollowingView(TemplateView):
    template_name = 'carrotStagram/following.html'

    def get(self, request, *args, **kwargs):
        if 'user' not in request.session.keys():
            return HttpResponseRedirect(reverse('carrotstagram:login'))
        ret = super().get(request, *args, **kwargs)
        return ret
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = get_account_info(self.request)
        context['account'] = account
        context['followings'] = account.follows.all()
        return context


class FollowerView(TemplateView):
    template_name = 'carrotStagram/followers.html'

    def get(self, request, *args, **kwargs):
        if 'user' not in request.session.keys():
            return HttpResponseRedirect(reverse('carrotstagram:login'))
        ret = super().get(request, *args, **kwargs)
        return ret
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = get_account_info(self.request)
        context['account'] = account
        context['followers'] = account.followers.all()
        return context



