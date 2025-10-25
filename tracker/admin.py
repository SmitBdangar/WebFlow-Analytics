from django.contrib import admin
from .models import Link, Click, VisitAudit

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('slug', 'creator', 'created_at', 'note')
    search_fields = ('slug', 'creator__username', 'note')


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('link', 'ts', 'ip', 'user_agent')
    search_fields = ('ip', 'user_agent')


@admin.register(VisitAudit)
class VisitAuditAdmin(admin.ModelAdmin):
    list_display = ('link', 'ts', 'user', 'note')
    search_fields = ('user__username', 'note')
