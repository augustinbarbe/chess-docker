"""Endpoints of the application"""

from flask import render_template, jsonify
import flask
import secrets
import redis

from . import app
from .task import launch_game

@app.route('/create', methods=['POST'])
def create():
    game_id = secrets.token_hex(nbytes=16)
    #launch_game.delay(game_id)

    return jsonify({"gameid":game_id}), 200, {'Content-Type': 'application/json'}
