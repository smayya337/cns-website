"""
URL configuration for acm_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views, settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/<int:year>/", views.past_officers, name="past_officers"),
    path("about/", views.about, name="about"),
    path("events/", views.events, name="events"),
    path("icpc/", views.icpc, name="icpc"),
    path("donate/", views.donate, name="donate"),
    path("hspc/", views.hspc, name="hspc"),
    path("users/<str:username>/", views.user_page, name="user_page"),
    path("events/<int:event>/", views.event_page, name="event_page"),
    path("accounts/logout/", views.logout_page, name="logout_page"),
    path("accounts/login/", views.login_page, name="login_page"),
    path("media/acm.png", views.redirect_media_to_static)  # hack
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
