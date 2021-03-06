from celery import Celery
from flask import Flask, request, abort
from flask.ext.cors import CORS
from .plugins import logging
import config
import os

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('config')
    if config:
        app.config.from_object(config)
    if 'ENV' in os.environ:
        app.config.from_object('config.{}'.format(os.environ['ENV']))

    logging.init_logging(app)

    from .api import Api
    Api(app)
    CORS(app)

    app.logger.info('App created')
    return app

celery_app = Celery('Minou2')
celery_app.config_from_object(config.celery)
