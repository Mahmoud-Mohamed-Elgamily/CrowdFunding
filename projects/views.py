from django.shortcuts import render, HttpResponse
from .models import Projects
# Create your views here.


def listProjects(req):
    context = {
        'projects': Projects.objects.all,
        'activate': 'projects',
        'tags' : Projects.objects.all().values('tag_id','tag_id__tag_name')
    }
    return render(req, 'projects/projects.html', context)


def singleProject(req, project_id):
    context = {
        'project' : Projects.objects.filter(id = project_id),
    }
    return render(req, 'projects/singleProject.html', context)
