from django.db import models

# Create your models here.
class Complaint(models.Model):
    # 投诉ID
    tousuid = models.CharField('投诉ID',max_length=10,blank=False, null=True)
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
    jbnr = models.TextField('举报内容',max_length=400,blank=True, null=True)
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
    # 催收描述
    csms = models.TextField('催收描述',max_length=200,null=True,blank=True)
    # 资料更新时间
    updated_at = models.DateTimeField('资料更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.tousuid