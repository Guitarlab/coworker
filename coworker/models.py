from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User


class Profile(models.Model):
    github_account_id = models.CharField(max_length=256)
    project = models.ForeignKey('Project')


class ProjectOwner(models.Model):
    profile = models.ForeignKey('Profile')
    project = models.ForeignKey('Project')


class ProjectHelper(models.Model):
    profile = models.ForeignKey('Profile')
    skill = models.ForeignKey('Skill')


class Skill(models.Model):
    skill_description = models.CharField(max_length=256)
    level = models.IntegerField()


class Project(models.Model):
    skill = models.ForeignKey('Skill')
    project_owner = models.ForeignKey('ProjectOwner')
    project_helper = models.ForeignKey('ProjectHelper')
    project_status = models.CharField(max_length=150)


class Issue(models.Model):
    project = models.ForeignKey('Project')
    issue_status = models.CharField(max_length=150)
    issue_link = models.CharField(max_length=150)
    issue_title = models.CharField(max_length=150)
    issue_description = models.CharField(max_length=150)
    issue_label = models.CharField(max_length=150)


class Milestone(models.Model):
    project = models.ForeignKey('Project')
    issue_status = models.CharField(max_length=150)
    issue_link = models.CharField(max_length=150)
    issue_title = models.CharField(max_length=150)
    issue_description = models.CharField(max_length=150)


# Create your models here.
# class GithubAccount(models.Model):
# user = models.ForeignKey('auth.User')
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
