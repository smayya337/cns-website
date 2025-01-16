from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(
        max_length=100, null=False, blank=False, help_text="Event name"
    )
    start = models.DateTimeField(
        default=timezone.now, help_text="Event start date and time"
    )
    end = models.DateTimeField(
        null=True, blank=True, help_text="Optional event end date and time"
    )
    location = models.CharField(
        max_length=30, null=False, blank=False, help_text="Event location"
    )
    description = models.TextField(
        null=False, blank=True, default="", help_text="Optional event description"
    )
    image = models.ImageField(
        upload_to="events/", default="acm.png", help_text="Event image"
    )

    def __str__(self):
        date_string = f"{self.start}"
        if self.end:
            date_string += f" - {self.end}"
        return f"{self.name}: {date_string} at {self.location}"


class Badge(models.Model):
    name = models.CharField(
        max_length=30, null=False, blank=False, unique=True, help_text="Badge name"
    )
    description = models.TextField(
        null=False, blank=True, help_text="Badge description"
    )
    color = models.CharField(
        max_length=16,
        null=False,
        blank=False,
        help_text="Badge color",
        choices=[
            ("blue", "Blue"),
            ("indigo", "Indigo"),
            ("purple", "Purple"),
            ("pink", "Pink"),
            ("red", "Red"),
            ("orange", "Orange"),
            ("yellow", "Yellow"),
            ("green", "Green"),
            ("teal", "Teal"),
            ("cyan", "Cyan"),
            ("black", "Black"),
            ("white", "White"),
            ("gray", "Gray"),
            ("gray-dark", "Dark Gray"),
        ],
        default="blue",
    )

    def __str__(self):
        return self.name


class User(AbstractUser):
    badges = models.ManyToManyField(Badge, blank=True)
    events_attended = models.ManyToManyField(Event, blank=True)
    image = models.ImageField(
        upload_to=f"users/",
        blank=True,
        help_text="A photo of the user",
        null=True,
        default="",
    )
    bio = models.TextField(
        null=False, blank=True, help_text="User's biography (Markdown is supported)"
    )
    hide = models.BooleanField(default=False, help_text="Hide this user")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Officer(models.Model):
    position = models.CharField(
        max_length=30, null=False, blank=False, help_text="Position"
    )
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
    user = ForeignKey(
        User, related_name="officers", on_delete=models.CASCADE, null=True, default=None
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.year}-{self.year + 1} {self.position})"

    class Meta:
        unique_together = ["year", "user"]


class CarouselImage(models.Model):
    image = models.ImageField(
        upload_to="carousel/", help_text="An image for the home page carousel"
    )
    label = models.CharField(
        max_length=30, null=False, blank=False, help_text="A label for the image"
    )
    caption = models.TextField(
        null=False,
        blank=True,
        default="",
        help_text="An optional extended caption for the image",
    )
    sort_order = models.IntegerField(
        default=0, help_text="Optional sort order of image"
    )

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Carousel image"
        verbose_name_plural = "Carousel images"


class HSPCContest(models.Model):
    year = models.IntegerField(unique=True, default=timezone.now().year)
    problem_set = models.FileField(
        upload_to="hspc/problems/", null=False, blank=False, help_text="Problem set PDF"
    )
    judge_data = models.FileField(
        upload_to="hspc/judge/",
        null=False,
        blank=False,
        help_text="Judge input/output ZIP",
    )

    def __str__(self):
        return f"{self.year}"

    class Meta:
        verbose_name = "HSPC contest"
        verbose_name_plural = "HSPC contests"


class NavBarLink(models.Model):
    url = models.CharField(
        max_length=150, null=False, blank=False, unique=True, help_text="Link to page"
    )
    label = models.CharField(
        max_length=30, null=False, blank=False, help_text="A label for the link"
    )
    sort_order = models.IntegerField(default=0, help_text="Optional sort order of link")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Navbar link"
        verbose_name_plural = "Navbar links"
