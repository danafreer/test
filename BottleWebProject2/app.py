"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

import os
import sys
from bottle import default_app, redirect, route, template

import zipfile

import danaemail

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    import bottle
    bottle.debug(True)



@route('/')
def hello():
    """Renders a sample page."""
    redirect('/hello/world')

@route('/hello/<name>')
def example(name):

    """Renders a sample page with the name specified in the URL."""

    danaemail.sendit()

    return template('<b>Hello there {{name}}</b>!', name=name)

import dana

@route('/dan')
def hellodan():

    z = zipfile.ZipFile("danazip.zip", "w")
    z.write("dana.py")
    return "Hello DAN!"

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return default_app()

if __name__ == '__main__':
    # Starts a local test server.
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    import bottle

    #PORT = 81

    bottle.run(server='wsgiref', host=HOST, port=PORT)
