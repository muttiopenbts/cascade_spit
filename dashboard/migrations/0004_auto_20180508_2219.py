# Generated by Django 2.0.5 on 2018-05-08 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_job_cmd_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='output',
            new_name='_output',
        ),
    ]
