from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.last_five_project, name="lastproject"),
    path('category/<int:id>', views.category_details, name="ProjectCategory"),
]

urlpatterns = [
    path('', views.all_projects, name="home"),
]
