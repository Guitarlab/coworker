from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from github import Github


def get_github_user(current_user):
    github_socialapp = SocialApp.objects.get(name='github app')
    current_socialaccount = SocialAccount.objects.get(user=current_user)
    social_token = SocialToken.objects.get(app=github_socialapp,
                                           account=current_socialaccount)
    current_token = social_token.token
    github_user = Github(current_token)
    return github_user


