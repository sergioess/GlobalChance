import os
import psycopg2

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://soauksyjoprrtk:298d2af34d644108c57364bffccc3a3d35aea9537a3f09fb57d2d3f47ad1f8f9@ec2-44-198-236-169.compute-1.amazonaws.com:5432/df25gu85pecij8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CARPETA_IMG = os.path.join('img')
CARPETA_PTOS = os.path.join('banner')


MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=587
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_USE_TLS = True
MAIL_USE_SSL = False

SESSION_TYPE = "filesystem"
SESSION_PERMANENT = False

