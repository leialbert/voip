from django import forms
from django.db import models
from django.db.models import fields

# Create your models here.
class Complaint(models.Model):
    # 投诉ID
    tousuid = models.CharField('投诉ID',max_length=10,blank=False, null=False,primary_key='tousuid',default='')
    # 来源渠道
    lyqd = models.CharField('来源渠道',max_length=20,blank=True, null=True)
    # 举报号码
    jbhm = models.CharField('举报号码',max_length=12,blank=True, null=True)
    # 被举报号码
    bjbhm = models.CharField('被举报号码',max_length=12,blank=True, null=True)
    # 举报号码运营商
    jbhmyys = models.CharField('举报号码运营商',max_length=12,blank=True, null=True)
    # 举报号码归属省份
    jbhmgssf = models.CharField('举报号码归属省份',max_length=12,blank=True, null=True)
    # 举报号码归属城市
    jbhmgscs = models.CharField('举报号码归属城市',max_length=12,blank=True, null=True)
    # 被举报号码归属省份
    bjbhmgssf = models.CharField('被举报号码归属省份',max_length=12,blank=True, null=True)
    # 被报号码归属城市
    bjbhmgscs = models.CharField('被报号码归属城市',max_length=12,blank=True, null=True)
    # 举报时间
    jb_date = models.DateTimeField('举报时间',blank=True, null=True)
    # 入库时间
    rk_date = models.DateTimeField('入库时间',blank=True, null=True)
    # 来电时间
    ld_date  = models.DateTimeField('来电时间',blank=True, null=True)
    # 不良类型
    bllx = models.CharField('不良类型',max_length=20,blank=True, null=True)
    # 通话时长
    thsc = models.CharField('通话时长',max_length=25, blank=True, null=True)
    # 被举报号码类型
    bjbhmlx = models.CharField('被举报号码类型',max_length=12,blank=True, null=True)
    # 举报内容
    jbnr = models.TextField('举报内容',max_length=1000,blank=True, null=True)
    # 投诉添加时间
    created_at = models.DateTimeField('投诉添加时间',auto_now_add=True, null=True)
    
    # 用户是谁
    who = models.CharField('用户是谁',max_length=10,blank=True,null=True)
    # 资料是否齐全
    is_cszl = models.BooleanField('资料是否齐全',default=False,null=True,blank=True)
    # 是否提交给移动
    is_tjyd = models.BooleanField('是否提交给移动',default=False,null=True,blank=True)
    # 催收机构名称
    csjg = models.CharField('催收机构名称',max_length=40,null=True,blank=True)
    # 被催收人
    bcsr = models.CharField('被催收人',max_length=40,null=True,blank=True)
    # 逾期金额
    yqje = models.FloatField('逾期金额',max_length=10,null=True,blank=True)
    # 逾期天数
    yqts = models.CharField('逾期天数',max_length=5,null=True,blank=True)
    # 投诉号码是否是本人
    is_br = models.BooleanField('投诉号码是否是本人',default=True)
    cszl_img = models.ImageField('借款资料',null=True, blank=True,upload_to='complaint/images/')
    cszl_mp3 = models.FileField('通话录音',null=True,blank=True,upload_to='complaint/files/')
    # 催收描述
    csms = models.TextField('催收描述',max_length=200,null=True,blank=True)
    # 资料更新时间
    updated_at = models.DateTimeField('资料更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.tousuid

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['cszl_img','cszl_mp3']