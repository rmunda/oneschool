# Register your models here.

# core/admin.py
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite
from .models import School

# Define a platform admin site
class CoreAdminSite(AdminSite):
    site_header = "OneSchool Platform Admin"
    site_title = "Platform Admin"
    index_title = "Manage Schools & Tenants"

core_admin_site = CoreAdminSite(name="core_admin")

# Register only platform-wide models here
core_admin_site.register(User)
core_admin_site.register(Group)
core_admin_site.register(School)

# @admin.register(School)
# class SchoolAdmin(admin.ModelAdmin):
#     list_display = ('name', 'domain', 'created_at')
#     search_fields = ('name', 'domain')

