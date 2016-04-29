from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from github import Github


# Create your views here.

def index(request):
    return render(request, 'coworker/index.html', {})


@login_required
def profile(request):
    current_user = request.user

    github_socialapp = SocialApp.objects.get(name='github app')
    current_socialaccount = SocialAccount.objects.get(user=current_user)
    social_token = SocialToken.objects.get(app=github_socialapp,
                                           account=current_socialaccount)
    current_token = social_token.token
    github_user = Github(current_token)
    params = {
        'login': github_user.get_user().login,

    }

    return render(request, 'coworker/profile.html', {'params': params})
