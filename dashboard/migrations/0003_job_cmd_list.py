# Generated by Django 2.0.5 on 2018-05-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_job_output'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='cmd_list',
            field=models.TextField(default='', help_text='Command separated list of command and parameters.'),
        ),
    ]
