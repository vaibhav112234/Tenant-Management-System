# Generated by Django 5.0.2 on 2024-04-11 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenantproject', '0005_main_username_sub_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanker',
            name='username',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
