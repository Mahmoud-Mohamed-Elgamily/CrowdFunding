from django.contrib import admin
from django.urls import path, include
from projects import urls as ProjectUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("HomePage.urls", namespace="crowdFund")),
    path('projects/', include(ProjectUrls)),
]
