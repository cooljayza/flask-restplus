from flask_restplus import Api
from flask import Blueprint

from .main.controller.math_controller import api as math_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(math_ns, path='/api/maths')
api.add_namespace(user_ns, path='/api/users')
