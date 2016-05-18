from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# from django.contrib.auth.models import User

class GithubProfile(models.Model):
    user = models.ForeignKey('auth.User')
    login = models.CharField(max_length=50)


class Project(models.Model):
    owner = models.ForeignKey('GithubProfile')
    title = models.CharField(max_length=100)


class Issue(models.Model):
    project = models.ForeignKey('Project')
    title = models.CharField(max_length=100)


class Relations(models.Model):
    profile = models.ForeignKey('GithubProfile')
    project = models.ForeignKey('Project')
    owner = models.BooleanField()

# class Profile(models.Model):
#     github_account_id = models.CharField(max_length=256)
#     project = models.ForeignKey('Project')
#
#
# class ProjectOwner(models.Model):
#     profile = models.ForeignKey('Profile')
#     project = models.ForeignKey('Project')
#
#
# class ProjectHelper(models.Model):
#     profile = models.ForeignKey('Profile')
#     skill = models.ForeignKey('Skill')
#
#
# class Skill(models.Model):
#     skill_description = models.CharField(max_length=256)
#     level = models.IntegerField()
#
#
# class Project(models.Model):
#     skill = models.ForeignKey('Skill')
#     project_owner = models.ForeignKey('ProjectOwner')
#     project_helper = models.ForeignKey('ProjectHelper')
#     project_status = models.CharField(max_length=150)
#
#
# class Issue(models.Model):
#     project = models.ForeignKey('Project')
#     issue_status = models.CharField(max_length=150)
#     issue_link = models.CharField(max_length=150)
#     issue_title = models.CharField(max_length=150)
#     issue_description = models.CharField(max_length=150)
#     issue_label = models.CharField(max_length=150)
#
#
# class Milestone(models.Model):
#     project = models.ForeignKey('Project')
#     issue_status = models.CharField(max_length=150)
#     issue_link = models.CharField(max_length=150)
#     issue_title = models.CharField(max_length=150)
#     issue_description = models.CharField(max_length=150)
