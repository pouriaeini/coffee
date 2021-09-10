from .base import *

ROOT_URLCONF = 'coffee.urls.admin'
INSTALLED_APPS += [
    'django.contrib.staticfiles',
    'django_better_admin_arrayfield',
]
