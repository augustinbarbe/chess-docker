""" Module containing asynchronous task to be ran"""
import docker

import secrets

from . import celery

def get_network_by_name(docker_client, name):
    """return the network object of the application"""
    networks = docker_client.networks.list()
    for nw in networks:
        if nw.name == name:
            return nw
    # TODO : create exception class
    raise Exception("Network hasn't been found.")


docker_client = docker.DockerClient()




@celery.task
def launch_container():
    """ Test docker"""
    game_id = secrets.token_hex(nbytes=16)
    bot_id = secrets.token_hex(nbytes=16)
    color = "white"

    arena_network = get_network_by_name(docker_client, "chessarena_default")

    cont = docker_client.containers.run('chess-ai',
                                        detach=True,
                                        environment=["COLOR_BOT=" + color,
                                                     "ID_BOT=" + bot_id,
                                                     "GAME_ID=" + game_id],
                                        network_mode=arena_network.name)

    

    return