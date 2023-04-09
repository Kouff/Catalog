import os

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

ALLOWED_HOSTS = []

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
