from django.http import Http404
from django.shortcuts import render
from django.utils import timezone

from acm_website.models import Officer, Event, CarouselImage, HSPCContest, User
from acm_website.settings import VENMO_LINK, ZELLE_LINK


def index(request):
    carousel_images = CarouselImage.objects.all()
    context = {"carousel_images": carousel_images}
    return render(request, "index.html", context)


def about(request):
    try:
        year = Officer.objects.order_by("-year")[0].year
    except IndexError:
        year = timezone.now().year
    past_years = sorted(
        list({o.year for o in Officer.objects.all() if o.year < year}), reverse=True
    )
    past_year_links = [
        {"year": f"{py}-{py + 1}", "link": f"/about/{py}"} for py in past_years
    ]
    officers = (
        Officer.objects.filter(year=year)
        .filter(faculty_advisor=False)
        .order_by("sort_order", "user")
    )
    advisors = (
        Officer.objects.filter(year=year)
        .filter(faculty_advisor=True)
        .order_by("sort_order", "user")
    )
    context = {
        "officers": officers,
        "advisors": advisors,
        "academic_year": f"{year}-{year + 1}",
        "past_years": past_year_links,
    }
    return render(request, "about.html", context)


def events(request):
    evts = Event.objects.filter(start__gte=timezone.now()).order_by("start")
    context = {
        "events": evts,
    }
    return render(request, "events.html", context)


def past_officers(request, year=timezone.now().year):
    officers = (
        Officer.objects.filter(year=year)
        .filter(faculty_advisor=False)
        .order_by("sort_order", "user")
    )
    advisors = (
        Officer.objects.filter(year=year)
        .filter(faculty_advisor=True)
        .order_by("sort_order", "user")
    )
    context = {
        "officers": officers,
        "advisors": advisors,
        "academic_year": f"{year}-{year + 1}",
    }
    if officers.count() == 0 and advisors.count() == 0:
        raise Http404()
    return render(request, "past_officers.html", context)


def icpc(request):
    return render(request, "icpc.html")


def donate(request):
    context = {"venmo": VENMO_LINK, "zelle": ZELLE_LINK}
    return render(request, "donate.html", context)


def hspc(request):
    past_sets = HSPCContest.objects.all().order_by("-year")
    context = {"past_sets": past_sets}
    return render(request, "hspc.html", context)


def user_page(request, user):
    user = User.objects.get(username=user)
    events_attended = user.events_attended.order_by("-start")
    badges = user.badges.all()
    if not user:
        raise Http404()
    context = {"user": user, "events_attended": events_attended, "badges": badges}
    return render(request, "user_page.html", context)
