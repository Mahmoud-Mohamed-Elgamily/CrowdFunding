from django.shortcuts import render , HttpResponse

# Create your views here.


def listProjects(req):
    # return HttpResponse("welcome")
    return render(req , 'projects/projects.html')
