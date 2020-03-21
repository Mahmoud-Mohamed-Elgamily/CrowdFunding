<<<<<<< HEAD
from django.shortcuts import render, HttpResponse, redirect
from .models import Projects, Donation, Tag
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = 'sk_test_kQeGPyzUEtnwIWuGkSSnkEYy00MTZcMDFF'
# publishkey 'pk_test_qldeOx2RsqvPXmVGAlXBlZQQ00qufvfDcj'
=======
from django.shortcuts import render, HttpResponse
from .models import Projects , Report ,Comment
from .form import CommentForm ,ReportForm
# Create your views here.
>>>>>>> a0f7889ee8d577a71d3af4d897c43d3ea09211b9


def listProjects(req):
    context = {
        'projects': Projects.objects.all,
        'activate': 'projects',
    }
    return render(req, 'projects/projects.html', context)


def singleProject(req, project_id):
    current_project = Projects.objects.get(id=project_id)
    tags_id = [t.id for t in current_project.tag.all()]

    context = {
        'project': current_project,
        'activate': 'projects',
        'similar': Projects.objects.filter(tag__in=tags_id).distinct()[:5],
    }

    return render(req, 'projects/singleProject.html', context)


def tagProjects(req, tag_name):
    context = {
        'projects': Projects.objects.filter(tag__tag_name=tag_name),
        'tag': tag_name
    }
    # print(context['project'])
    return render(req, 'projects/tagProjects.html', context)


def charge(req):
    print('Data:', req.POST)

    # amount = int(req.POST['amount'])
    project_id = req.POST['project_id']
    # print(project_id)
    # customer = stripe.Customer.create(
    #     source=req.POST['stripeToken']
    # )

    # donation = Donation.create(
    #     project_id=customer,
    #     user_id = current user ,
    #     donation_amount=amount*100
    # )

    return redirect(f"/projects/{project_id}", 'success')
def selectProject(req,id):
    project = Projects.objects.filter(id = int(id)).first()
    comments = Comment.objects.filter(project_id=project)
    comment = None
  
    if project:
        if req.method == 'POST':
            comment_form = CommentForm(req.POST)
            if comment_form.is_valid():
                comment_content=req.POST.get("comment_content")
           
                comment=Comment.objects.create(project_id=project,comment_content=comment_content)
                comment.save()
              
        else:
            comment_form = CommentForm()
            
        return render(req,"projects/singleProject.html",{ "project" :project,
        "comments":comments,
        "comment_form":comment_form,
       })

    else:
        return HttpResponse("404 Not Found")

def reportProject(req ):
    project = Projects.objects.filter()
    reports = Report.objects.filter()
    if req.method == 'POST':
            report_form = ReportForm(req.POST or None)
            if report_form.is_valid():
                report_content=req.POST.get("report_content")
            
                report=Report.objects.create(project_id=project,report_content=report_content)
                report.save()
                
    else:
        report_form = ReportForm()
            
    return render(req,"projects/report.html",{
        "reports":reports,
    "report_form":report_form,
   })

