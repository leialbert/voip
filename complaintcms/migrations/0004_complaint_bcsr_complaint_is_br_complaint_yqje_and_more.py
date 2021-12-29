# Generated by Django 4.1.dev20211224190413 on 2021-12-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaintcms', '0003_alter_complaint_jbnr'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='bcsr',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='被催收人'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='is_br',
            field=models.BooleanField(default=True, null=True, verbose_name='投诉号码是否是本人'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='yqje',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='逾期金额'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='yqts',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='逾期天数'),
        ),
    ]
