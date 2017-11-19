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
def launch_container(game_id):
    """ Asynchrously start a container with the id""" 
    white_id = secrets.token_hex(nbytes=16)
    black_id = secrets.token_hex(nbytes=16)

    arena_network = get_network_by_name(docker_client, "chessarena_default")

    whit = docker_client.containers.run('chess-ai',
                                        detach=True,
                                        environment=["WHITE_ID=" + white_id,
                                                     "BLACK_ID=" + black_id,
                                                     "COLOR=white",
                                                     "GAME_ID=" + game_id],
                                        network_mode=arena_network.name)

    cont = docker_client.containers.run('chess-ai',
                                        detach=True,
                                        environment=["WHITE_ID=" + white_id,
                                                    "BLACK_ID=" + black_id,
                                                    "COLOR=black",
                                                    "GAME_ID=" + game_id],
                                    network_mode=arena_network.name)



    return