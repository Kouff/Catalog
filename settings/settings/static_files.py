import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

STATIC_URL = 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
