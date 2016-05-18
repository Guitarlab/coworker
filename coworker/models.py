from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# from django.contrib.auth.models import User

class GithubProfile(models.Model):
    user = models.ForeignKey('auth.User')
    login = models.CharField(max_length=50, unique=True)


class Repository(models.Model):
    owner = models.ForeignKey('GithubProfile')
    name = models.CharField(max_length=100)
    github_id = models.IntegerField(unique=True)


class Issue(models.Model):
    repository = models.ForeignKey('Repository')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    github_id = models.IntegerField(unique=True)


class Relation(models.Model):
    profile = models.ForeignKey('GithubProfile')
    repository = models.ForeignKey('Repository')
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
