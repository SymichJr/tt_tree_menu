import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tt_tree_menu.settings")

application = get_wsgi_application()
