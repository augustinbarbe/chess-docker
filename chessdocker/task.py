""" Module containing asynchronous task to be ran"""
import docker

from . import celery

docker_client = docker.from_env()

@celery.task
def launch_container():
    print(docker_client.images.list())
