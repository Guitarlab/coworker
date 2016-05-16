from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from coworker.models import Relations
from . import github_api


# Create your views here.

def index(request):
    return render(request, 'coworker/index.html', {})


def project_list(request):
    projects = Relations.objects.filter(owner=True)
    return render(request, 'coworker/project_list.html', {'projects': projects})


@login_required
def profile(request):
    current_user = request.user
    github_account = github_api.get_github_account(current_user)

    # save to session
    request.session['github_account'] = github_account

    github_user = github_account.get_user()

    return render(request, 'coworker/profile.html', {'github_user': github_user})


@login_required
def choose_project(request):
    github_account = request.session['github_account']
    repos = github_account.get_user().get_repos()
    return render(request, 'coworker/choose_project.html', {'repos': repos})


@login_required
def add_project(request, rep_id):
    github_account = request.session['github_account']
    # TODO: add exception
    rep = github_account.get_repo(int(rep_id))
    if request.method == "POST":
        print(request.POST)
        relation = Relations()
        relation.profile = request.user
        relation.project_id = int(rep_id)
        relation.owner = True
        relation.save()
        return HttpResponse(content=rep.id)

    if github_account.get_user().id == rep.owner.id:
        issues = rep.get_issues()
        return render(request, 'coworker/add_project.html', {'rep': rep, 'issues': issues})
    else:
        return HttpResponse("You can add only your own project!")
