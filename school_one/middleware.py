import os

from django.conf import settings

from .utils import set_current_school_db, clear_current_school_db

from django.shortcuts import redirect
from django.urls import reverse

from dotenv import load_dotenv

load_dotenv()


class SchoolDBMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            db_alias = self.resolve_school_db(request)
            set_current_school_db(db_alias)
            response = self.get_response(request)
        finally:
            # Always clean up, even if exception occurs
            clear_current_school_db()
        return response

    def resolve_school_db(self, request):
        """
        Determines the DB alias for the current school based on subdomain.
        Example:
            abc.schoolplatform.com --> school_abc
            schoolplatform.com -> default
        """
        # if settings.DEBUG:
        #     dev_school = os.getenv("DJANGO_DEV_SCHOOL", "default")
        #     print('Dev school: ', dev_school)
        #     return f'school_{dev_school}'
        host = request.get_host().split(':')[0]  # Remove port if any
        print('Host from middleware', host)
        parts = host.split('.')
        print('Domain parts' , len(parts))

        # Handle cases where subdomain exists
        if len(parts) >= 2:
            subdomain = parts[0]
            print(f'Database route key school_{subdomain}')
            return f'school_{subdomain}'

        # No subdomain → default DB
        return 'default'


class RestrictCoreAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]  # abc.oneschool
        if host != "oneschool" and request.path.startswith("/admin/"):
            # Block core admin on tenant subdomains
            return redirect("/school-admin/")  # or return 404
        return self.get_response(request)
