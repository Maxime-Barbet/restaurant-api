from flask_testing import TestCase
from app.main import db
from manage import app

from app.main.model.restaurant import Restaurant


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        restaurant1 = Restaurant(
            id=1,
            name="Le Bonobo café",
            address="66 rue d’Hauteville, Paris, France 75010"
        )
        restaurant2 = Restaurant(
            id=2,
            name="Wild and Wood Coffee",
            address="47 London Wall, London, United Kingdom EC2M 5TE"
        )
        db.session.add(restaurant1)
        db.session.add(restaurant2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()