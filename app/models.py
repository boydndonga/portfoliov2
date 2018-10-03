from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    projects = db.relationship('Project', backref='category', lazy='dynamic')


    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),unique = True,index = True)
    projects = db.relationship('Project', backref='category', lazy='dynamic')

    def __repr__(self):
        return f'Category {self.name}'

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    def delete_category(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories
    
Class Project(db.model):
    __tablename__= 'projects'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))