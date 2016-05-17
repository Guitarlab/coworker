from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# latest models:

# class Profile(models.Model):
#    github_account_id = models.CharField(max_length=256)
#    is_active = models.BooleanField(default=True)
#    skills = models.ForeignKey('Skill')
#
#
# class Skill(models.Model):
#    skill_description = models.CharField(max_length=256)
#    level = models.IntegerField()
#
#
# class Project(models.Model):
#    skill = models.ForeignKey('Skill')
#    project_owner = models.ForeignKey('Profile')
#    project_helper = models.ManyToManyField('Profile')
#    project_link = models.CharField(max_length=150)
#    project_status = models.CharField(max_length=150)
#    is_active = models.BooleanField(default=True)
#
#
# class Issue(models.Model):
#    project = models.ForeignKey('Project')
#    issue_status = models.CharField(max_length=150)
#    issue_link = models.CharField(max_length=150)
#    issue_title = models.CharField(max_length=150)
#    issue_description = models.CharField(max_length=150)
#    issue_label = models.CharField(max_length=150)


# previous version models:

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
