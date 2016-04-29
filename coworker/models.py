from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User



# Create your models here.
# class GithubAccount(models.Model):
#     user = models.ForeignKey('auth.User')
#     login = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     token = models.CharField(max_length=50, blank=True, null=True)
#
#     # repositories
#     # issues
#
#
#     def set_token(self):
#         github_socialapp = SocialApp.objects.get(name='github app')
#         current_socialaccount = SocialAccount.objects.get(user=self.user)
#         current_token = SocialToken.objects.get(app=github_socialapp,
#                                                 account=current_socialaccount)
#         self.token = current_token
#         self.save()
#
#     def set_email(self):
