from django.contrib import admin
from .models import Complaint
# Register your models here.

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    fields = ('tousuid','jbhm','bjbhm','bllx','ld_date','thsc','jbnr','who','csjg','bcsr','yqje','yqts','is_br','csms','is_cszl','is_tjyd')
    list_display = ('tousuid','jbhm','bllx','ld_date','thsc','who','is_cszl','is_tjyd')