from django.shortcuts import render

# Create your views here.

from projects.models import *


def all_projects (request):
    all_projects = Projects.objects.all()

    context ={

        "allProjects":all_projects
    }
    return render(request,"homepage.html",context)

