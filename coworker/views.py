from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken


# Create your views here.


def index(request):
    return render(request, 'coworker/index.html', {})


@login_required
def profile(request):
    current_user = request.user
    github_socialapp = SocialApp.objects.get(name='github app')
    current_socialaccount = SocialAccount.objects.get(user=current_user)
    current_token = SocialToken.objects.get(app=github_socialapp,
                                            account=current_socialaccount)
    print(current_user.id)
    return render(request, 'coworker/profile.html', {'id': id})
