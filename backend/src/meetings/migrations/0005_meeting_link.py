# Generated by Django 4.1.1 on 2023-01-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0004_rename_choosen_time_meeting_chosen_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting", name="link", field=models.URLField(null=True),
        ),
    ]
