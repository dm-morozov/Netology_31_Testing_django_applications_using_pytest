"""
WSGI config for Netology_31_Testing_django_applications_using_pytest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Netology_31_Testing_django_applications_using_pytest.settings')

application = get_wsgi_application()
