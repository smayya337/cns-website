# Generated by Django 4.2.14 on 2024-07-28 21:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        (
            "acm_website",
            "0009_carouselimage_sort_order_alter_carouselimage_caption_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(
                blank=True, default="", help_text="Optional event description"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="end",
            field=models.DateTimeField(
                blank=True, help_text="Optional event end date and time", null=True
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                default="acm.png", help_text="Optional event image", upload_to="events/"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.CharField(help_text="Event location", max_length=30),
        ),
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(help_text="Event name", max_length=30),
        ),
        migrations.AlterField(
            model_name="event",
            name="start",
            field=models.DateTimeField(
                default=django.utils.timezone.now, help_text="Event start date and time"
            ),
        ),
    ]
