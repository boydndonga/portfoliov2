import unittest
from flask import current_app
from app import create_app,db
from app.models import User


class UserModelTESTCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client
        self.new_user = User(username='boyde', email='boyde@gmaile.com', password='walaisijui')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_instance_var(self):
        self.assertAlmostEquals(self.new_user.username,'boyde')