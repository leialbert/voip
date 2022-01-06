from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('result/',views.result,name='result'),
    path('parse/',views.parse, name='parse'),
    path('saveto/',views.saveto, name='saveto'),
    # path('upload/',views.upload,name='upload'),
]