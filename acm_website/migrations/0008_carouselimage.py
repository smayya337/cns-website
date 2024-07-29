# Generated by Django 4.2.14 on 2024-07-28 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acm_website", "0007_alter_officer_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarouselImage",
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
                ("image", models.ImageField(upload_to="carousel/")),
                ("label", models.CharField(max_length=30)),
                ("caption", models.TextField(blank=True, default="")),
            ],
        ),
    ]
