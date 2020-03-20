from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile,UserPhone
from projects.models import Projects

# Create your views here.


@login_required()
def show_profile(request):
    # profile = Profile.user
    # phone = profile.phone_set.all()
    return render(request, 'user/profile.html')


def edit_profile(request):
    form = UserChangeForm()
    return render(request, 'user/edit_profile.html', {'form': form})


def my_projects(request):
    my_project = Projects.object.filter(user_id=User.id)
    return render(request, 'user/my_projects.html')


def delete_profile(request):
    return render(request,'user/delete_profile.html')