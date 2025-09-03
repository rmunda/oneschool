# Create your models here.

# core/models.py
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

# Extend user model
class User(AbstractUser):
    school_code = models.CharField(max_length=50, null=True, blank=True)
    # e.g. 'abc', 'xyz'
    # is_superadmin = models.BooleanField(default=False)  # platform-wide superadmin

class School(models.Model):
    name = models.CharField(max_length=255)
    db_name = models.CharField(max_length=100, unique=True)  # Unique DB alias per tenant
    domain = models.CharField(max_length=255, unique=True)   # Optional for subdomain mapping
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

