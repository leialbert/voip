from django.contrib import admin
from .models import Complaint,DownloadComplaint
# Register your models here.

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('tousuid','jbhm','bllx','ld_date','thsc','who','is_cszl','is_tjyd')
    list_filter = ('ld_date','who','bllx','is_cszl','is_tjyd')
    search_fields = ('tousuid','jbhm','bjbhm')
    list_per_page = 10

@admin.register(DownloadComplaint)
class DownloadComplaintAdmin(admin.ModelAdmin):
    list_display = ('img1','img2','img3','mp3_wav')
    list_per_page = 10