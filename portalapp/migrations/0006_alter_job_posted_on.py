# Generated by Django 3.2 on 2021-05-26 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0005_auto_20210526_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
