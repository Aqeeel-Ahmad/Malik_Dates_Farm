import os
import sys

# Ensure project root is in sys.path for Vercel Serverless Function execution
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from config.wsgi import app
