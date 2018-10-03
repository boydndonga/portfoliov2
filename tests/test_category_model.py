import unittest
from flask import current_app
from app import create_app,db
from app.models import Category


class CategoryModelTESTCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client
        self.new_category = Category(name='networking')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_category_instance_var(self):
        self.assertEqual(self.new_category.name,'networking')
