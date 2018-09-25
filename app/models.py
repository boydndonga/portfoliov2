from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    pass