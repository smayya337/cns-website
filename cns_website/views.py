from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils import timezone

from cns_website.forms import LoginForm, ProfileForm
from cns_website.models import Officer, Event, CarouselImage, User


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
        list(
            {o.year for o in Officer.objects.filter(user__hide=False) if o.year < year}
        ),
        reverse=True,
    )
    past_year_links = [
        {"year": f"{py}-{py + 1}", "link": f"/about/{py}"} for py in past_years
    ]
    officers = (
        Officer.objects.filter(year=year)
        .filter(faculty_advisor=False)
        .filter(user__hide=False)
        .order_by("sort_order", "user")
    )
    advisors = (
        Officer.objects.filter(year=year)
        .filter(faculty_advisor=True)
        .filter(user__hide=False)
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
        .filter(user__hide=False)
        .order_by("sort_order", "user")
    )
    advisors = (
        Officer.objects.filter(year=year)
        .filter(faculty_advisor=True)
        .filter(user__hide=False)
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


# def icpc(request):
#     return render(request, "icpc.html")


# def donate(request):
#     context = {"venmo": VENMO_LINK, "zelle": ZELLE_LINK}
#     return render(request, "donate.html", context)


# def hspc(request):
#     past_sets = HSPCContest.objects.all().order_by("-year")
#     context = {"past_sets": past_sets}
#     return render(request, "hspc.html", context)


def user_page(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        if not user or user.hide:
            return HttpResponseBadRequest()
        if request.user.is_authenticated:
            if request.user.username == username:
                form = ProfileForm(request.POST, request.FILES)
                if form.is_valid():
                    if form.cleaned_data["image"]:
                        user.image = form.cleaned_data["image"]
                    elif form.cleaned_data["image"] is False:
                        user.image = ""
                    user.bio = form.cleaned_data["bio"]
                    user.save()
                    messages.add_message(
                        request, messages.SUCCESS, "Your profile has been updated!"
                    )
                    return redirect(request.path)
                else:
                    messages.add_message(
                        request, messages.ERROR, "Unable to update profile! Try again."
                    )
                    return redirect(request.path)
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "You are not authorized to update this profile!",
                )
                return redirect(request.path)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "You are not authorized to update this profile!",
            )
            return redirect(request.path)
    else:
        if not user or user.hide:
            raise Http404()
        events_attended = user.events_attended.order_by("-start")
        badges = user.badges.all()
        form = ProfileForm()
        form.fields["image"].initial = user.image
        form.fields["bio"].initial = user.bio
        context = {
            "req_user": user,
            "events_attended": events_attended,
            "badges": badges,
            "form": form,
        }
        return render(request, "user_page.html", context)


def event_page(request, event):
    event = Event.objects.get(pk=event)
    attendees = event.user_set.filter(hide=False)
    event_happened = timezone.now() >= event.start
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user in attendees:
                event.user_set.remove(request.user)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "You've been removed from the attendees list for this event.",
                )
            else:
                event.user_set.add(request.user)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "You've been added to the attendees list for this event.",
                )
            event.save()
        else:
            messages.add_message(request, messages.ERROR, "You're not signed in!")
        return redirect("event_page", event.pk)
    else:
        context = {
            "event": event,
            "attendees": attendees,
            "event_happened": event_happened,
        }
        return render(request, "event_page.html", context)


def logout_page(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "You have been logged out!")
    return redirect("index", permanent=True)


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        nxt = request.POST["next"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "You are now logged in!")
            return redirect(nxt, permanent=True)
        else:
            messages.add_message(
                request, messages.ERROR, "Invalid username or password!"
            )
            return redirect(f"{request.path}?next={nxt}")
    else:
        nxt = request.GET.get("next", "/")
        form = LoginForm()
        form.fields["next"].initial = nxt
        context = {"nxt": nxt, "form": form}
        return render(request, "login_page.html", context)


# Horrendously hacky, I know
def redirect_media_to_static(request):
    path = request.path
    path = path.removeprefix("/media")
    path = "/static" + path
    return redirect(path)
