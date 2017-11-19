"""Endpoints of the application"""

from flask import render_template
import flask
import secrets

from . import app
from .task import launch_container

@app.route('/create', methods=['POST'])
def create():
    game_id = secrets.token_hex(nbytes=16)
    launch_container.delay(game_id)
    return flask.Response(status=204)
