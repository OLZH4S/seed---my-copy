# Generated by Django 4.1.1 on 2023-01-23 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0005_alter_meeting_choosen_time_alter_meeting_founder_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Meeting",),
    ]
