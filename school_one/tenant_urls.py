from .tenant_admin import tenant_admin_site
from django.urls import path

urlpatterns = [
    path("school-admin/", tenant_admin_site.urls),
]
