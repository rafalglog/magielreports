"""
WSGI config for magiel_raport_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
os.environ["DJANGO_SETTINGS_MODULE"] = "{{magiel_raport_main}}.settings"
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/

"""

import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magiel_raport_main.settings")


application = get_wsgi_application()
