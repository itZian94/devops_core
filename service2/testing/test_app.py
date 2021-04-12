from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from service2.app import app
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRand(TestBase):
    def test_randintgen(self):
        randnum =self.client.get(url_for('randintgen', randnum=2647))