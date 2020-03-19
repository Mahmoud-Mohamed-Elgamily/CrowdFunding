from django.conf.urls import url
from django.urls import path
from . import views

app_name ="HomePage"
urlpatterns = [

    url(r'^$', views.last_five_project, name="lastproject"),
    path('category/<int:id>', views.category_details, name="ProjectCategory"),
]
