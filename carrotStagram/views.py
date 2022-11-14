from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import *
from carrotStagram.models import *

# Create your views here.
def loginView(request):
    if request.method == 'GET':
        return render(request, 'carrotStagram/login.html')
    elif request.method == 'POST':
        accountname = request.POST.get('accountname', None)
        password = request.POST.get('accountpw', None)

    error_message = {}
    if not (accountname and password):
        error_message['error'] = "올바르지 않은 id/pw입니다"
    else:
        try:
            account = Account.objects.get(name=accountname)
            if password == account.password:
                request.session ['user'] = account.id
                return HttpResponseRedirect(reverse('carrotstagram:friend'))
            else:
                error_message['error']='올바르지 않은 id/pw입니다'
        except:
            error_message['error']='올바르지 않은 id/pw입니다'
    return render(request,'carrotStagram/login.html', error_message)

def settingView(request):
    pass

class FriendView(ListView):
    pass

class FeedView(ListView):
    pass

class MyPageView(DetailView):
    pass

class PostDetailView(DetailView):
    pass

class FollowingView(ListView):
    pass

class FollowerView(ListView):
    pass


