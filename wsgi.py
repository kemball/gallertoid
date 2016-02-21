#!/usr/bin/python
import os

#virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'),'virtenv')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from gallertoid import app as application

#
# Below for testing only
#
if __name__ == '__main__':
    SQL_ALCHEMY_DATABASE_URI= "mysql://adminsX4kPYt:lmX8jFYZpEVj@localhost/gallertoid"
    from wsgiref.simple_server import make_server
    application.debug=True
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    print "Server started, request away"

    httpd.serve_forever()
