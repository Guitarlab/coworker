from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from coworker.github_api import get_github_user


# Create your views here.

def index(request):
    return render(request, 'coworker/index.html', {})


@login_required
def profile(request):
    current_user = request.user
    github_user = get_github_user(current_user)

    # save to session
    request.session['github_user'] = github_user

    params = {
        'login': github_user.get_user().login,

    }
    return render(request, 'coworker/profile.html', {'params': params})


def choose_project(request):
    pass
