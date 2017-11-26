""" Module containing asynchronous task to be ran"""
import docker
import secrets
import redis
from . import celery

docker_client = docker.DockerClient()

def get_network_by_name(docker_client, name):
    """return the network object of the application"""
    networks = docker_client.networks.list()
    for nw in networks:
        if nw.name == name:
            return nw
    # TODO : create exception class
    raise Exception("Network hasn't been found.")


@celery.task
def launch_game(game_id):
    """ Asynchrously start a container with the id""" 

    # TODO : ugly hardcoding of the network name. Make it parametric
    arena_network = get_network_by_name(docker_client, "chessarena_default")

    whit = docker_client.containers.run('chess-ai',
                                        detach=True,
                                        environment=["COLOR=white",
                                                     "GAME_ID=" + game_id],
                                        network_mode=arena_network.name)

    blac = docker_client.containers.run('chess-ai',
                                        detach=True,
                                        environment=["COLOR=black",
                                                     "GAME_ID=" + game_id],
                                        network_mode=arena_network.name)


    return