from django.core.validators import EmailValidator
from django.db import models
from django.utils import timezone


class Officer(models.Model):
    first_name = models.CharField(
        max_length=30, null=False, blank=False, help_text="First name"
    )
    last_name = models.CharField(
        max_length=30, null=False, blank=False, help_text="Last name"
    )
    position = models.CharField(
        max_length=30, null=False, blank=False, help_text="Position"
    )
    bio = models.TextField(null=False, blank=True, help_text="Officer's biography (Markdown is supported)")
    sort_order = models.IntegerField(
        default=0, help_text="Optional sort order of officer"
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        default=timezone.now().year,
        help_text="The year this officer was elected",
    )
    faculty_advisor = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        help_text="Whether this person is a faculty advisor",
    )
    email = models.EmailField(null=False, blank=False, help_text="UVA email address")
    image = models.ImageField(
        upload_to=f"officers/", blank=True, help_text="A photo of the officer"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.year}-{self.year + 1} {self.position})"


class Event(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, help_text="Event name")
    start = models.DateTimeField(default=timezone.now, help_text="Event start date and time")
    end = models.DateTimeField(null=True, blank=True, help_text="Optional event end date and time")
    location = models.CharField(max_length=30, null=False, blank=False, help_text="Event location")
    description = models.TextField(null=False, blank=True, default="", help_text="Optional event description")
    image = models.ImageField(upload_to="events/", default="acm.png", help_text="Event image")

    def __str__(self):
        date_string = f"{self.start}"
        if self.end:
            date_string += f" - {self.end}"
        return f"{self.name}: {date_string} at {self.location}"


class CarouselImage(models.Model):
    image = models.ImageField(upload_to="carousel/", help_text="An image for the home page carousel")
    label = models.CharField(max_length=30, null=False, blank=False, help_text="A label for the image")
    caption = models.TextField(null=False, blank=True, default="",
                               help_text="An optional extended caption for the image")
    sort_order = models.IntegerField(default=0, help_text="Optional sort order of image")

    def __str__(self):
        return self.label


class HSPCContest(models.Model):
    year = models.IntegerField(unique=True, default=timezone.now().year)
    problem_set = models.FileField(upload_to="hspc/problems/", null=False, blank=False, help_text="Problem set PDF")
    judge_data = models.FileField(upload_to="hspc/judge/", null=False, blank=False, help_text="Judge input/output ZIP")

    def __str__(self):
        return f"{self.year}"
