import unittest
from flask import current_app
from app import create_app,db
from app.models import Project,User,Category
from datetime import datetime


class ProjectModelTESTCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client
        self.new_user = User(username='boyde', email='boyde@gmaile.com', password='walaisijui')
        self.new_category = Category(name='networking')
        self.new_project = Project(title='projo', description='ufala mob tu',
                            timestamp=datetime.utcnow,user_id=self.new_user.id,category=self.new_category)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_project_instance_var(self):
        self.assertEqual(self.new_project.title,'projo')
        self.assertEqual(self.new_project.description,'ufala mob tu')
        self.assertEqual(self.new_project.timestamp,datetime.utcnow)
        self.assertEqual(self.new_project.user_id,self.new_user)
        self.assertEqual(self.new_project.category,self.new_category)
