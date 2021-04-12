from service1.app import app, db, Keyword
#from service1.app import db
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                )
        return app

    def setUp(self):
        db.create_all()

        sample_keyword=Keyword(value="abc123456")

        db.session.add(sample_keyword)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestDat(TestBase):
    def test_dat_get(self):
        response=self.client.get(url_for('homepage'))
        self.assertNotEqual(response.status_code, 200)

