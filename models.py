# Models python File

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        