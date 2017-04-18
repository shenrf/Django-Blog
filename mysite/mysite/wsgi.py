"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
>>>>>>> d77f5829752f031379513206e62b4778083c0009
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
