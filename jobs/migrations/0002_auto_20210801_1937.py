# Generated by Django 3.2.5 on 2021-08-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='posted_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]