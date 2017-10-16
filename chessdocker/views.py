"""Endpoints of the application"""

from flask import render_template
import flask

from . import app
from .task import launch_container

@app.route('/create', methods=['POST'])
def create():
    launch_container.delay()
    return flask.Response(status=204)
