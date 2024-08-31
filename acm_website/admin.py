from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Officer, Event, CarouselImage, HSPCContest, NavBarLink, User

admin.site.register(User, UserAdmin)
admin.site.register(Officer)
admin.site.register(Event)
admin.site.register(CarouselImage)
admin.site.register(HSPCContest)
admin.site.register(NavBarLink)
