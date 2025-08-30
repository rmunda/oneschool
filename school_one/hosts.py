# one_school/hosts.py
from django_hosts import patterns, host

host_patterns = patterns('',
    # www.oneschool → routes to myproject/urls.py
    host(r'www', 'school_one.urls', name='www'),

    # <subdomain>.oneschool → routes to tenant/urls.py
    host(r'(?P<tenant>[\w-]+)', 'school_one.tenant_urls', name='tenant'),

    # admin.oneschool → routes to myproject/admin_urls.py
    #host(r'admin', 'myproject.urls', name='admin'),
)
