from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from service4.app import app
import requests

class  TestBase(TestCase):
    def create_app(self):
        return app

class TestResult(TestBase):
    def test_complete_result(self):
        response =self.client.get(url_for('complete_result', randnum=2))