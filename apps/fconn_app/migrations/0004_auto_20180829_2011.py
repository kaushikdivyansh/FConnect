# Generated by Django 2.1 on 2018-08-29 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fconn_app', '0003_auto_20180829_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='user',
            new_name='student',
        ),
    ]