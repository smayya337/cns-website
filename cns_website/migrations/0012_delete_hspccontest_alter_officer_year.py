# Generated by Django 4.2.18 on 2025-01-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cns_website", "0011_alter_event_name"),
    ]

    operations = [
        migrations.DeleteModel(
            name="HSPCContest",
        ),
        migrations.AlterField(
            model_name="officer",
            name="year",
            field=models.IntegerField(
                default=2025, help_text="The year this officer was elected"
            ),
        ),
    ]
