# Generated by Django 4.0 on 2022-01-08 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_kehu_company_doc_kehu_contract_kehu_other_doc_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kehu',
            new_name='Zhanghu',
        ),
        migrations.AlterModelOptions(
            name='gateway',
            options={'verbose_name_plural': '3 - 网关管理'},
        ),
        migrations.AlterModelOptions(
            name='huasu',
            options={'verbose_name_plural': '4 - 话术管理'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name_plural': '2 - 缴费记录'},
        ),
        migrations.AlterModelOptions(
            name='zhanghu',
            options={'verbose_name_plural': '1 - 账号信息'},
        ),
    ]
