# Generated by Django 2.2.12 on 2020-05-26 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0004_auto_20200526_1029"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="candidatevote", options={"verbose_name": "Candidate vote", "verbose_name_plural": "Canditate votes"},
        ),
    ]