from flask_restplus import Api
from flask import Blueprint

from app.main.controller.restaurant_controller import api as restaurant_namespace

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='RESTAURANT API',
          version='0.1'
          )

api.add_namespace(restaurant_namespace, path='/restaurants')