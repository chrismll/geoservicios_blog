# geoservicios_blog/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoservicios_blog.settings')

application = get_asgi_application()