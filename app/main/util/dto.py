from flask_restplus import Namespace, fields


class RestaurantDto:
    api = Namespace('restaurant', description='restaurant related operations')
    user = api.model('restaurant', {
        'name': fields.String(required=True, description='restaurant name'),
        'address': fields.String(required=True, description='restaurant address')
    })