from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def show_profile(request):
    # return HttpResponse("Welcome.. user profile")
    user = User.objects.filter(username='mariam')
    return render(request, 'user/profile.html', {'user': user})


def edit_profile(request):
    form = UserChangeForm()
    return render(request, 'user/edit_profile.html', {'form': form})


def my_projects(request):
    return render(request, 'user/my_projects.html')


def delete_profile(request):
    return render(request,'user/delete_profile.html')