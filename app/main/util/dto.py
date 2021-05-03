from flask_restplus import Namespace, fields
import enum

class AlgorithmEnum(enum.Enum):
    forLoop = 'FOR_LOOP'
    whileLoop = 'WHILE_LOOP'
    recursion = 'RECURSION'

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'gender': fields.String(required=True, description='user gender'),
        'random_value': fields.String(required=False, description='random value'),
        'ip_address': fields.String(required=True, description='user ip address'),
        'id': fields.String(description='user Identifier')
    })
    users = api.model('users',{
        'users': fields.List(fields.Nested(user))
    })
    groupedUsers = api.model('grouped_users', {
        'type': fields.String(description='gender type'),
        'people': fields.List(fields.Nested(user))
    })
    

class NumbersDto:
    api = Namespace('maths', description='math related operations')
    numbers = api.model('numbers', {
        'numbers': fields.List(fields.Integer)
    })
    algorithm = api.model('algorithm', {
        'algorithm': fields.String(enum=[x.value for x in AlgorithmEnum], attribute='algorithm.value')
    })



