from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from coworker.models import GithubProfile, Repository, Issue, Relation
from coworker.github_api import get_github_account


# Create your views here.

def index(request):
    return render(request, 'coworker/index.html', {})


def project_list(request):
    relations = Relation.objects.filter(owner=True)
    return render(request, 'coworker/project_list.html', {'relations': relations})


# first view (redirecting after oauth login)
# filling models: (github profile, project , issue)
@login_required
def profile(request):
    # working with github api for populating models
    current_user = request.user
    github_account = get_github_account(current_user)


    # Load user info (profile, projects, issues) from Github

    # GithubProfile Model
    github_user = github_account.get_user()
    gp, gp_created = GithubProfile.objects.get_or_create(user=current_user,
                                                         login=github_user.login)

    # Repository Model
    repos = github_user.get_repos()
    for rep in repos:
        r, r_created = Repository.objects.get_or_create(owner=gp,
                                                        name=rep.name,
                                                        github_id=rep.id)
        # Issue Model
        issues = rep.get_issues(state='open')
        for issue in issues:
            Issue.objects.get_or_create(repository=r,
                                        title=issue.title,
                                        github_id=issue.id,
                                        state=issue.state,
                                        body=issue.body)
    # now we can use django queries!
    user = GithubProfile.objects.get(user=current_user)

    return render(request, 'coworker/profile.html', {'user': user})


@login_required
def choose_project(request):
    repos = Repository.objects.all()
    return render(request, 'coworker/choose_project.html', {'repos': repos})


@login_required
def add_project(request, rep_id):
    rep = Repository.objects.get(id=rep_id)
    github_profile = GithubProfile.objects.get(user=request.user)

    if request.method == "POST":
        relation, relation_created = Relation.objects.get_or_create(profile=github_profile,
                                                                    repository=rep,
                                                                    owner=True)
        return HttpResponse(content=rep.id)

    if github_profile == rep.owner:
        issues = rep.issue_set.all()
        return render(request, 'coworker/add_project.html', {'rep': rep, 'issues': issues})
    else:
        return HttpResponse("You can add only your own project!")
