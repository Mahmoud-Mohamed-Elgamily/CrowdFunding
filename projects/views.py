from django.shortcuts import render, HttpResponse
from .models import Projects
# Create your views here.


def listProjects(req):
    context = {
        'projects': Projects.objects.all,
        'activate': 'projects',
    }
    return render(req, 'projects/projects.html', context)


def singleProject(req, project_id):
    current_project = Projects.objects.get(id = project_id)
    context = {
        'project' : current_project,
        'similar' : Projects.objects.filter(tag__in=current_project.tag.all)
    }
    print(current_project.tag__tag_name)
    return render(req, 'projects/singleProject.html', context)

def tagProjects(req , tag_name):
    context = {
        'projects' : Projects.objects.filter(tag__tag_name=tag_name),
        'tag' : tag_name
    }
    # print(context['project'])
    return render(req, 'projects/tagProjects.html', context)
