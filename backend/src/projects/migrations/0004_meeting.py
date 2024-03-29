# Generated by Django 4.1.1 on 2023-01-23 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_alter_project_end_date_alter_project_project_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meeting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("option_1_time", models.DateTimeField()),
                ("option_2_time", models.DateTimeField()),
                ("option_3_time", models.DateTimeField()),
                ("description", models.CharField(max_length=100)),
                ("is_accepted", models.BooleanField(default=False)),
                ("project", models.SlugField(unique=True)),
                ("invitee", models.EmailField(max_length=254, unique=True)),
                ("choosen_time", models.DateTimeField(blank=True, null=True)),
                (
                    "founder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]
