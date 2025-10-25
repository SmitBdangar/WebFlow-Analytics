from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.http import HttpResponse
from .models import Link, Click
import uuid
import requests
from decimal import Decimal
from django.contrib.auth.decorators import login_required


# Generate a random 10-character slug
def make_slug():
    return uuid.uuid4().hex[:10]

def get_client_ip(request):
    """
    Get client IP address from request headers.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

from django.shortcuts import redirect

def home_redirect(request):
    return redirect('login')


@login_required(login_url='login')
def main_page(request):
    """
    Admin page where police officer can generate links and see recent clicks.
    """
    generated_link = None

    if request.method == "POST":
        case_name = request.POST.get("case_name")
        if case_name:
            # Create a new Link
            link = Link.objects.create(
                slug=make_slug(),
                case_name=case_name,
                creator=request.user
            )
            # Build full URL for the generated link
            generated_link = request.build_absolute_uri(f"/go/{link.slug}/")

    # Get all clicks for links created by this user
    clicks = Click.objects.filter(link__creator=request.user).select_related('link').order_by('-ts')

    return render(request, "tracker/main.html", {
        "generated_link": generated_link,
        "clicks": clicks,
    })


def tracking_view(request, slug):
    link = get_object_or_404(Link, slug=slug)
    ip = get_client_ip(request)
    user_agent = request.META.get("HTTP_USER_AGENT", "")

    # lookup location
    geo = lookup_geoip(ip)

    # create click with geo fields
    Click.objects.create(
        link=link,
        ip=ip,
        user_agent=user_agent,
        city=geo.get("city",""),
        region=geo.get("region",""),
        country=geo.get("country",""),
        latitude=geo.get("latitude"),
        longitude=geo.get("longitude"),
    )

    return redirect("/public_page/")



def public_page(request):
    """
    Simple public page everyone is redirected to.
    """
    return render(request, "tracker/public_page.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_page")
        else:
            return render(request, "tracker/login.html", {"error": "Invalid credentials"})
    return render(request, "tracker/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# tracker/views.py (add these imports near top)


# helper: detect private/local IPs
PRIVATE_PREFIXES = ("10.", "172.", "192.168.", "127.", "169.254.")

def is_private_ip(ip):
    if not ip:
        return True
    for p in PRIVATE_PREFIXES:
        if ip.startswith(p):
            return True
    return False

def lookup_geoip(ip):
    """
    Return dict: city, region, country, latitude, longitude
    Uses ipapi.co free endpoint as a simple solution.
    """
    result = {"city":"", "region":"", "country":"", "latitude": None, "longitude": None}
    if not ip or is_private_ip(ip):
        return result  # local/private IPs won't geolocate

    try:
        # ipapi.co example: https://ipapi.co/8.8.8.8/json/
        resp = requests.get(f"https://ipapi.co/{ip}/json/", timeout=3)
        if resp.status_code == 200:
            data = resp.json()
            result["city"] = data.get("city", "") or ""
            result["region"] = data.get("region", "") or ""
            result["country"] = data.get("country_name", "") or ""
            lat = data.get("latitude") or data.get("lat")
            lon = data.get("longitude") or data.get("lon")
            if lat is not None and lon is not None:
                try:
                    result["latitude"] = Decimal(str(lat))
                    result["longitude"] = Decimal(str(lon))
                except Exception:
                    result["latitude"] = None
                    result["longitude"] = None
    except Exception:
        # network error or service error — silently fail and return empty result
        pass

    return result
