# Generated by Django 4.1.1 on 2023-01-24 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0002_alter_meeting_choosen_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="project",
            field=models.CharField(default="Project Name", max_length=255),
        ),
    ]