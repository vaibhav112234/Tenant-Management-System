# Generated by Django 5.0.2 on 2024-04-11 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenantproject', '0003_remove_tenant_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='username',
            field=models.CharField(default='0', max_length=100),
        ),
    ]