# Generated by Django 4.0 on 2021-12-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaintcms', '0007_complaint_cszl_img_alter_complaint_cszl_mp3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='cszl_img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/', verbose_name='借款资料'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='cszl_mp3',
            field=models.FileField(blank=True, null=True, upload_to='uploads/files/', verbose_name='通话录音'),
        ),
    ]
