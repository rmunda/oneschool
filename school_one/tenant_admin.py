# school_one/tenant_admin.py
from django.contrib.admin import AdminSite
from apps.teachers.models import Teacher
#from apps.students.models import Student

class TenantAdminSite(AdminSite):
    site_header = "Tenant Admin"
    site_title = "Tenant Portal"
    index_title = "Welcome to Tenant Admin"

tenant_admin_site = TenantAdminSite(name="tenant_admin")

# Register tenant-specific models
tenant_admin_site.register(Teacher)
#tenant_admin_site.register(Student)
