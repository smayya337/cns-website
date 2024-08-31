from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Officer, Event, CarouselImage, HSPCContest, NavBarLink, User, Badge

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "bio", "image")}),
        (_("ACM status"), {"fields": ("events_attended", "badges")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Officer)
admin.site.register(Event)
admin.site.register(CarouselImage)
admin.site.register(HSPCContest)
admin.site.register(NavBarLink)
admin.site.register(Badge)
