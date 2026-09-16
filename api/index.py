import os
import sys
import traceback

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from config.wsgi import application

def handler(environ, start_response):
    try:
        return application(environ, start_response)
    except Exception as e:
        tb = traceback.format_exc()
        print("ERROR IN WSGI HANDLER:\n", tb)
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        return [f"<h1>Deployment Error (500)</h1><pre>{tb}</pre>".encode('utf-8')]

app = handler
