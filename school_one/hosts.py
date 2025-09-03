# one_school/hosts.py
from django_hosts import patterns, host

host_patterns = patterns('',
                         # www.oneschool → routes to school_one/urls.py
                         host(r'www', 'school_one.urls', name='www'),
                         host(r'oneschool', 'school_one.urls', name='root'),

                         # <subdomain>.oneschool → routes to school_one/tenant_urls.py
                         host(r'(?P<tenant>[\w-]+)', 'school_one.tenant_urls', name='tenant'),

                         # admin.oneschool → routes to myproject/admin_urls.py
                         # host(r'admin', 'myproject.urls', name='admin'),
                         )
