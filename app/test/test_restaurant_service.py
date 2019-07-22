import json
import pytest
from app.test.base import BaseTestCase

from app.main.service.restaurant_service import save_restaurant, delete_restaurant, get_restaurants, get_restaurant
from app.main.model.restaurant import Restaurant


params = {
    'test_save_restaurant': [
        {
            'restaurant_object': {'name': 'Starbucks Opéra', 'address': '26 Avenue de l\'Opera, Paris, France 75001'},
            'response_object': {'status': 'success', 'message': 'Successfully created.'},
            'http_code': 201
        },
        {
            'restaurant_object': {'name': 'Le Bonobo café', 'address': '66 rue d’Hauteville, Paris, France 75010'},
            'response_object': {'status': 'fail', 'message': 'Restaurant already exists.'},
            'http_code': 409
        }
    ],
    'test_delete_restaurant': [
        {
            'name': 'Le Bonobo café',
            'response_object': {'status': 'success', 'message': 'Successfully deleted.'},
            'http_code': 204
        },
        {
            'name': 'Starbucks Opéra',
            'response_object': {'status': 'fail', 'message': 'Restaurant does not exist.'},
            'http_code': 404
        }
    ],
    'test_get_restaurants': [
        Restaurant(
            id=1,
            name="Le Bonobo café",
            address="66 rue d’Hauteville, Paris, France 75010"
        ),
        Restaurant(
            id=2,
            name="Wild and Wood Coffee",
            address="47 London Wall, London, United Kingdom EC2M 5TE"
        )
    ],
    'test_get_restaurant': [
        {
            'name': 'Le Bonobo café',
            'restaurant': Restaurant(
                id=1,
                name="Le Bonobo café",
                address="66 rue d’Hauteville, Paris, France 75010"
            )
        },
        {'name': 'Starbucks Opéra', 'restaurant': None}
    ]
}


class TestRestaurantService(BaseTestCase):

    def test_save_restaurant(self):
        for line in params['test_save_restaurant']:
            sr_response_object, sr_http_code = save_restaurant(line['restaurant_object'])
            assert line['response_object'] == sr_response_object
            assert line['http_code'] == sr_http_code


    def test_delete_restaurant(self):
        for line in params['test_delete_restaurant']:
            sr_response_object, sr_http_code = delete_restaurant(line['name'])
            assert line['response_object'] == sr_response_object
            assert line['http_code'] == sr_http_code

    def test_get_restaurants(self):
        restaurants = get_restaurants()
        assert len(params['test_get_restaurants']) == len(restaurants)
        assert params['test_get_restaurants'] == restaurants

    def test_get_restaurant(self):
        for line in params['test_get_restaurant']:
            restaurant = get_restaurant(line['name'])
            assert line['restaurant'] == restaurant