from setuptools import setup

setup(
    name='chessdocker',
    packages=['chessdocker'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-redis',
        'docker',
    ],
)
