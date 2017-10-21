""" Module containing asynchronous task to be ran"""
import docker

from . import celery

docker_client = docker.DockerClient()

@celery.task
def launch_container():
    """ Test docker"""
    print(docker_client.images.list())
    print(docker_client.containers.\
                    run("ubuntu", "echo hello world"))
