# Register your models here.

# core/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import School

User = get_user_model()


class CoreAdminSite(AdminSite):
    site_header = "OneSchool Platform Admin"
    site_title = "Platform Admin"
    index_title = "Manage Schools & Tenants"


core_admin_site = CoreAdminSite(name="core_admin")


@admin.register(User, site=core_admin_site)
class CustomUserAdmin(BaseUserAdmin):
    # Modify fieldsets: add school_code inside the "General" section
    fieldsets = tuple(
        (name, dict(opts, fields=opts["fields"] + ("school_code",)))
        if name is None or name == "General" else (name, opts)
        for name, opts in BaseUserAdmin.fieldsets
    )

    # Same for add_fieldsets
    add_fieldsets = tuple(
        (name, dict(opts, fields=opts["fields"] + ("school_code",)))
        if name is None else (name, opts)
        for name, opts in BaseUserAdmin.add_fieldsets
    )

    list_display = ("username", "email", "school_code", "is_staff", "is_active")
    search_fields = ("username", "email", "school_code")


core_admin_site.register(Group)
core_admin_site.register(School)

# @admin.register(School)
# class SchoolAdmin(admin.ModelAdmin):
#     list_display = ('name', 'domain', 'created_at')
#     search_fields = ('name', 'domain')
