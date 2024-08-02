from .models import NavBarLink


def get_nav_bar_links(request):
    links = NavBarLink.objects.all().order_by("sort_order")
    return {"links": links}
