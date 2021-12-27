# voip URL Configuration
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('complaint/', include('complaintcms.urls')),
    path('admin/', admin.site.urls),
]
