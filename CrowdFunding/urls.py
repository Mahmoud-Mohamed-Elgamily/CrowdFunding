from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from projects import urls as ProjectUrls
from userAuth import urls as userUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("HomePage.urls", namespace="crowdFund")),
    path('', include("HomePage.urls")),
    path('projects/', include(ProjectUrls)),
    path('profile/', include(userUrls)),
    path('user/', include("user.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
