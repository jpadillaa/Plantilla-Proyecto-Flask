'''
Setup - Python packages para la API 
Nota: Agregue los paquetes adicionales que uso para el desarrollo de su proyecto
'''
from setuptools import setup

setup(
    name='api',
    packages=['api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'marshmallow-sqlalchemy',
        'flask-restful',
        'flask-marshmallow',
        'flask-jwt-extended',
        'python-dotenv',
        'psycopg2-binary',
        'marshmallow_enum'
    ],
)