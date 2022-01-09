from django.db import models
from django.db.models.deletion import CASCADE

# 账户信息
class Zhanghu(models.Model):
    KH_CHOICES = ['普通账户','结算账户']
    class Meta:
        verbose_name_plural = "1 - 账号信息"
    zhanghao = models.CharField('账号',max_length=20,primary_key=True)
    zhanghu = models.CharField('账户',max_length=40)
    balance = models.FloatField('余额',max_length=10)
    zh_type = models.Choices('账户类型',KH_CHOICES)
    company_doc = models.FileField('营业执照',null=True,blank=True,upload_to='crms/files/')
    contract = models.FileField('合同',null=True,blank=True,upload_to='crms/files/')
    other_doc = models.FileField('补充附件',null=True,blank=True,upload_to='crms/files/')
    tel_phone = models.CharField('联系方式',max_length=40,default='')

    def __str__(self):
        return self.zhanghu
class Payment(models.Model):
    class Meta:
        verbose_name_plural = "2 - 缴费记录"
    charge_date = models.DateTimeField('缴费时间',auto_now=True, null=True)
    charge_acc = models.ForeignKey('Zhanghu',on_delete=CASCADE,verbose_name='缴费金额')
    before_charge = models.FloatField('缴费前余额',max_length=20)
    after_charge = models.FloatField('缴费后余额',max_length=20)
# 网关管理
class Gateway(models.Model):
    class Meta:
        verbose_name_plural = "3 - 网关管理"
    GATEWAY_CHOICES = ['对接账户','落地网关']
    name = models.CharField('网关名称',max_length=100)
    gateway_type = models.Choices('网关类型',GATEWAY_CHOICES)
    rate = models.CharField('费率',max_length=20)
    prefix = models.ForeignKey('Zhanghu',on_delete=CASCADE,verbose_name='网关前缀')

    def __str__(self):
        return self.name

class Huasu(models.Model):
    class Meta:
        verbose_name_plural = '4 - 话术管理'
    title = models.CharField('话术名称',max_length=40)
    content = models.TextField('话术内容', max_length=800)
    is_approved = models.BooleanField('是否审核通过',default=False)
    def __str__(self):
        return self.title

