import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from config.wsgi import application

# Auto-migrate SQLite on serverless startup if tables don't exist yet
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
except Exception:
    pass

app = application
