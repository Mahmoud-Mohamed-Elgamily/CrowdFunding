from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_profile , name="profile"),
    path('edit/', views.edit_profile),
    path('delete/', views.delete_profile),
    path('my_projects/', views.my_projects)
]
