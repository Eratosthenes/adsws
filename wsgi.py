# -*- coding: utf-8 -*-
"""
    wsgi
    ~~~~

    adsws wsgi module
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from adsws import api
from adsws import frontend

application = DispatcherMiddleware(frontend.create_app(), {
    '/api': api.create_app()
})

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=False, use_debugger=True)
