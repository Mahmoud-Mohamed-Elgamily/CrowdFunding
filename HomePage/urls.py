from django.conf.urls import url
from . import views

app_name ="HomePage"
urlpatterns = [

    url(r'^$',views.all_projects,name="all_projects"),


]

