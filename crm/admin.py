from django.contrib import admin
from .models import Zhanghu,Gateway,Huasu,Payment
# Register your models here.
@admin.register(Zhanghu)
class ZhanghuAdmin(admin.ModelAdmin):
    list_display = ('zhanghao','zhanghu','balance')
    # list_filter = ('ld_date','who','bllx','is_cszl','is_tjyd')
    # search_fields = ('tousuid','jbhm','bjbhm')
    list_per_page = 10
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('charge_date','charge_acc','before_charge','after_charge')
    # list_filter = ('ld_date','who','bllx','is_cszl','is_tjyd')
    # search_fields = ('tousuid','jbhm','bjbhm')
    list_per_page = 10
@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ('name','gateway_type','rate','prefix')
    # list_filter = ('ld_date','who','bllx','is_cszl','is_tjyd')
    # search_fields = ('tousuid','jbhm','bjbhm')
    list_per_page = 10
@admin.register(Huasu)
class HuasuAdmin(admin.ModelAdmin):
    list_display = ('title','is_approved')
    # list_filter = ('ld_date','who','bllx','is_cszl','is_tjyd')
    # search_fields = ('tousuid','jbhm','bjbhm')
    list_per_page = 10