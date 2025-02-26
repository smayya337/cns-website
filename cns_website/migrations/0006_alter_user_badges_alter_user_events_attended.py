# Generated by Django 4.2.14 on 2024-08-31 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cns_website", "0005_remove_officer_bio_remove_officer_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="badges",
            field=models.ManyToManyField(blank=True, null=True, to="cns_website.badge"),
        ),
        migrations.AlterField(
            model_name="user",
            name="events_attended",
            field=models.ManyToManyField(blank=True, null=True, to="cns_website.event"),
        ),
    ]
