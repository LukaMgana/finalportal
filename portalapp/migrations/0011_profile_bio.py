# Generated by Django 3.2 on 2021-07-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0010_auto_20210710_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Hi, say something..', max_length=500),
        ),
    ]