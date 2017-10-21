""" Module containing asynchronous task to be ran"""
import docker

from . import celery

@celery.task
def launch_container():
    print(docker_client.images.list())
