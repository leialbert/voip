# voip URL Configuration
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from complaintcms.views import index
urlpatterns = [
    path('',index),
    path('complaint/', include('complaintcms.urls',namespace='complaintcms')),
    path('crm/', include('crm.urls',namespace='crm')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)