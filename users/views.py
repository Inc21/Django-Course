from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


def login_user(request):
    """
    Login page view
    """

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['username']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def logout_user(request):
    """
    Logout view
    """
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')


def profiles(request):
    """
    view
    """
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    """
    view
    """
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)
