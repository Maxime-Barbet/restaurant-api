from flask import request
from flask_restplus import Resource

from app.main.util.dto import RestaurantDto
from app.main.service.restaurant_service import save_restaurant, delete_restaurant, get_restaurants, get_restaurant, get_random_restaurant

api = RestaurantDto.api
_restaurant = RestaurantDto.user


@api.route('/')
class RestaurantList(Resource):
    @api.doc('list of restaurants')
    @api.marshal_list_with(_restaurant)
    def get(self):
        """List all restaurants"""
        return get_restaurants()

    @api.response(201, 'Restaurant successfully created.')
    @api.doc('create a new restaurant')
    @api.expect(_restaurant, validate=True)
    def post(self):
        """Creates a new restaurant """
        data = request.json
        return save_restaurant(data=data)


@api.route('/<name>')
@api.param('name', 'The Restaurant name')
@api.response(404, 'Restaurant not found.')
class Restaurant(Resource):
    @api.doc('get a restaurant')
    @api.marshal_with(_restaurant)
    def get(self, name):
        """get a restaurant given its name"""
        restaurant = get_restaurant(name)
        if not restaurant:
            api.abort(404)
        else:
            return restaurant

    @api.response(204, 'Restaurant successfully deleted.')
    @api.doc('delete a restaurant')
    def delete(self, name):
        """delete a restaurant given its name"""
        restaurant = get_restaurant(name)
        if not restaurant:
            api.abort(404)
        return delete_restaurant(name)


@api.route('/random')
@api.response(404, 'Restaurant not found.')
class RandomRestaurant(Resource):
    @api.doc('get a random restaurant')
    @api.marshal_with(_restaurant)
    def get(self):
        """get a restaurant given its name"""
        restaurant = get_random_restaurant()
        if not restaurant:
            api.abort(404)
        return restaurant