import json
from app.test.base import BaseTestCase
from app.main.controller.restaurant_controller import RestaurantList, Restaurant

params = {
    'test_restaurant_list_get': {
        'restaurants': [
            {'name': 'Le Bonobo café', 'address': '66 rue d’Hauteville, Paris, France 75010'},
            {'name': 'Wild and Wood Coffee', 'address': '47 London Wall, London, United Kingdom EC2M 5TE'}
        ],
        'status_code': 200
    },
    'test_restaurant_list_post': [
        {
            'restaurant_object': {'name': 'Starbucks Opéra', 'address': '26 Avenue de l\'Opera, Paris, France 75001'},
            'status_code': 201
        },
        {
            'restaurant_object': {'name': 'Le Bonobo café', 'address': '66 rue d’Hauteville, Paris, France 75010'},
            'status_code': 409
        }
    ],
    'test_restaurant_get': [
        {
            'name': 'Le Bonobo café',
            'restaurant': {'name': 'Le Bonobo café', 'address': '66 rue d’Hauteville, Paris, France 75010'},
            'status_code': 200
        },
        {
            'name': 'Starbucks Opéra',
            'restaurant': None,
            'status_code': 404
        }
    ],
    'test_restaurant_delete': [
        {
            'name': 'Le Bonobo café',
            'status_code': 204
        },
        {
            'name': 'Starbucks Opéra',
            'status_code': 404
        }
    ]
}

class TestRestaurantController(BaseTestCase):

    def test_restaurant_list_get(self):
        restaurant_response = self.client.get('/restaurants/')
        self.assertEqual(params['test_restaurant_list_get']['restaurants'], restaurant_response.json)
        self.assertEqual(params['test_restaurant_list_get']['status_code'], restaurant_response.status_code)

    def test_restaurant_list_post(self):
        for line in params['test_restaurant_list_post']:
            restaurant_response = self.client.post(
                '/restaurants/',
                data=json.dumps(line['restaurant_object']),
                content_type='application/json'
            )
            self.assertEqual(line['status_code'], restaurant_response.status_code)

    def test_restaurant_get(self):
        for line in params['test_restaurant_get']:
            restaurant_response = self.client.get('/restaurants/' + line['name'])
            self.assertEqual(line['status_code'], restaurant_response.status_code)
            if restaurant_response.status_code != 404:
                self.assertEqual(line['restaurant'], restaurant_response.json)

    def test_restaurant_delete(self):
        for line in params['test_restaurant_delete']:
            restaurant_response = self.client.delete('/restaurants/' + line['name'])
            self.assertEqual(line['status_code'], restaurant_response.status_code)