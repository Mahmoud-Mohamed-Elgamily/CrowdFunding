from django.shortcuts import render, HttpResponse
from . models import User

# Create your views here.

def showProfile(request):
    # return HttpResponse("Welcom.. user profile")
    return render(request, "user/profile.html")


