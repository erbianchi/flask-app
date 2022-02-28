from flask import Flask, url_for, request, render_template, g
from markupsafe import escape

from werkzeug.middleware.proxy_fix import ProxyFix

import os, os.path
import time, math

app = Flask(__name__)
app.jinja_env.cache = {}

@app.route('/')
@app.route('/index')
def index():
    ## Slowing down everything
    start = time.time()
    x = 0.0001
    for _ in iter(range(100000)):
        x += math.sqrt(x)

    parameters = {}
    parameters['cloudfront_path'] = "/static"
    parameters['time_elapsed_secs'] = round(time.time() - start, 5)

    return render_template('index.html', parameters=parameters)

@app.route('/ping')
def ping():
    return "OK"

app.wsgi_app = ProxyFix(app.wsgi_app)
