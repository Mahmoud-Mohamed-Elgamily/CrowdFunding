from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("HomePage.urls", namespace="crowdFund")),
    path('', include("HomePage.urls")),
    path('projects/', include("projects.urls")),
    path('profile/', include("userAuth.urls")),
    path('user/', include("user.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
