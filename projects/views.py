from django.shortcuts import render, HttpResponse, redirect
from .models import Projects, Donation, Tag
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = 'sk_test_kQeGPyzUEtnwIWuGkSSnkEYy00MTZcMDFF'
# publishkey 'pk_test_qldeOx2RsqvPXmVGAlXBlZQQ00qufvfDcj'


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
