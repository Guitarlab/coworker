from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import github_api


# Create your views here.

def index(request):
    return render(request, 'coworker/index.html', {})


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
    return render(request, 'coworker/add_project.html', {'rep': rep_id})
