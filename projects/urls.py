from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.listProjects , name= "projects" ),
    path('charge', views.charge , name= "charge" ),
    path('<project_id>', views.singleProject , name= "singleProject" ),
    path('tag/<tag_name>', views.tagProjects , name= "tags" ),
]
