from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings
import uuid

User = get_user_model()

def make_slug():
    return uuid.uuid4().hex[:10]  # 10-char random slug

class Link(models.Model):
    slug = models.CharField(max_length=32, default=make_slug, unique=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    case_name = models.CharField(max_length=200)  # <-- add this
    note = models.TextField(blank=True)  # optional extra note

    def __str__(self):
        return f"{self.slug} ({self.case_name})"



class Click(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="clicks")
    ts = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=100)
    user_agent = models.TextField(blank=True)

    # New geolocation fields
    city = models.CharField(max_length=150, blank=True)
    region = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=150, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        ordering = ["-ts"]

    def __str__(self):
        return f"{self.ts} {self.ip} ({self.link.slug})"

class VisitAudit(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    ts = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.ts} {self.user} {self.link.slug}"
