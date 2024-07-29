# Generated by Django 4.2.14 on 2024-07-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acm_website", "0003_remove_officer_name_officer_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="officer",
            name="faculty_advisor",
            field=models.BooleanField(
                default=False, help_text="Whether this person is a faculty advisor"
            ),
        ),
    ]
