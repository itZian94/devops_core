from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from service3.app import app
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAlpha(TestBase):
    def test_randalphagen(self):
        loweralpha= ('h', 'z', 'c')
        randomalpha = loweralpha
        assert any(randomalpha) == True
    def test_randalphagen(self):
        upperalpha = ('H', 'Z')
        randomalpha = upperalpha
        assert any(randomalpha) == True
