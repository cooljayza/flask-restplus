from werkzeug.utils import cached_property
from flask import request
from flask_restplus import Resource

from ..util.dto import NumbersDto, AlgorithmEnum
from ..service.math_service import closestToZero, sumOfNumbersForLoop, sumOfNumbersRecursion, sumOfNumbersWhileLoop

api = NumbersDto.api
_numbers = NumbersDto.numbers
_algorithms = NumbersDto.algorithm


@api.route('/closest-to-zero')
class ClosestToZero(Resource):
    @api.doc('finds closest number to zero')
    @api.expect(_numbers, validate=True)
    def post(self):
        """Finds closest number to zero """
        data = request.json
        return closestToZero(data['numbers'])

@api.route('/sum-of-numbers/<algorithm>')
@api.param('algorithm', 'The algorithm to use for computing the sum')
class SumOfNumbers(Resource):
    @api.doc('sums up all the numbers')
    @api.expect(_numbers, validate=True)
    def post(self,algorithm):
        """Sums up numbers given an algorithm"""
        data = request.json['numbers']
        if algorithm ==  AlgorithmEnum.forLoop.value:
            return sumOfNumbersForLoop(data)
        elif algorithm == AlgorithmEnum.whileLoop.value:
            return sumOfNumbersWhileLoop(data)
        elif algorithm == AlgorithmEnum.recursion.value:
            return sumOfNumbersRecursion(data)
        api.abort(406,"Unsupported Algorithm. Supported Algorithms: WHILE_LOOP, FOR_LOOP, RECURSION")