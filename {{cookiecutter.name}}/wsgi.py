"""Web handlers of the project."""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.name}}.settings')

application = get_wsgi_application()
