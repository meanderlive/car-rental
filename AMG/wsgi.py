"""
WSGI config for AMG project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
path=r'/home/mspl/Pictures/car-rental-main/'
if path not in sys.path:
    sys.path.append(path)


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AMG.settings')

application = get_wsgi_application()

