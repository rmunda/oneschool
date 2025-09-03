# core/auth_backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from school_one.utils import get_current_school_db

User = get_user_model()


class SchoolBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            print('User', user)
        except User.DoesNotExist:
            return None
        # print((user.check_password(password)))
        if user.check_password(password) and self.user_can_authenticate(user):
            print('User after authentication', user)
            return user
        print('Returning none')
        return None

    def user_can_authenticate(self, user):
        subdomain = get_current_school_db().split('_')[1] if not get_current_school_db()=='default' else None
        print('Thread local database route', subdomain)
        print('Current subdomain', subdomain)
        print('Current school code', user.school_code)

        if user.is_superuser:
            return True  # super admin can log in anywhere

        if user.school_code and subdomain == user.school_code:
            print('Allowed..')
            return True

        print('Denied..')
        return False
