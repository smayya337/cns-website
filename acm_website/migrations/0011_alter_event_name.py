# Generated by Django 4.2.14 on 2024-10-30 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acm_website", "0010_alter_badge_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(help_text="Event name", max_length=100),
        ),
    ]
