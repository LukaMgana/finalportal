# Generated by Django 3.2 on 2021-05-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0006_alter_job_posted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
