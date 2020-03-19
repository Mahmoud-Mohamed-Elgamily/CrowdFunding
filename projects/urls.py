from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.listProjects , name= "projects" ),
    path('<project_id>', views.singleProject , name= "singleProject" ),
]
