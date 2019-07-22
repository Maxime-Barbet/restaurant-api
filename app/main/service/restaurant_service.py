import uuid
import datetime

from app.main import db
from app.main.model.restaurant import Restaurant

from sqlalchemy import func


def save_restaurant(data):
    restaurant = Restaurant.query.filter_by(name=data['name']).first()
    if not restaurant:
        new_restaurant = Restaurant(
            name=data['name'],
            address=data['address']
        )
        save_changes(new_restaurant)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Restaurant already exists.',
        }
        return response_object, 409


def delete_restaurant(name):
    restaurant = Restaurant.query.filter_by(name=name).first()
    if restaurant:
        delete_changes(restaurant)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
        }
        return response_object, 204
    else:
        response_object = {
            'status': 'fail',
            'message': 'Restaurant does not exist.'
        }
        return response_object, 404


def get_restaurants():
    return Restaurant.query.all()


def get_restaurant(name):
    return Restaurant.query.filter_by(name=name).first()


def get_random_restaurant():
    return Restaurant.query.order_by(func.random()).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()