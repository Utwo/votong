# Generated by Django 2.2.16 on 2020-10-07 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0025_auto_20201006_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='politic_members',
        ),
    ]
