from werkzeug.utils import cached_property
from flask import request, jsonify, make_response,Response
from flask_restplus import Resource
from json2xml import json2xml

from ..util.dto import UserDto
from ..model.user_model import convertUsersDictToArray
from ..service.user_service import groupByGender

api = UserDto.api
_users = UserDto.users
_grouped_users = UserDto.groupedUsers

@api.route('/group-by-gender')
class GroupUser(Resource):
    @api.doc('groups users by gender')
    @api.marshal_list_with(_grouped_users, envelope='data')
    @api.expect(_users, validate=True)
    def post(self):
        """Groups users by gender and add random value """
        data = request.json
        users = convertUsersDictToArray(data['users'])
        
        return groupByGender(users)
