from django.contrib import admin
from .models import Complaint
# Register your models here.

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('tousuid','jbhm','bllx','ld_date','thsc','who','is_cszl','is_tjyd')
    list_filter = ('ld_date','who','bllx','is_cszl','is_tjyd')
    search_fields = ('tousuid','jbhm','bjbhm')
    list_per_page = 10