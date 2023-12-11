"""
WSGI config for UniVerse project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UniVerse.settings')

# Get the WSGI application
application = get_wsgi_application()

# Wrap the application with WhiteNoise
application = WhiteNoise(application)

# Add the path to your static files (change 'static' to your actual static folder)
application.add_files(os.path.join(os.path.dirname(__file__), 'static'), prefix='static/')
