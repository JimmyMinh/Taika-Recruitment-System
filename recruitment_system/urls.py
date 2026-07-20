from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),


path('', include('jobs.urls')),

path('applications/', include('applications.urls')),

path('users/', include('users.urls')),

path('interviews/', include('interviews.urls')),


]


urlpatterns += static(
settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT
)
