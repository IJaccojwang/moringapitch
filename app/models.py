from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import admin


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self, author, quote):
        self.author = author
        self.quote = quote


class User():

    def __init__(self, username, email, bio, password):

        self.username = username
        self.email = email
        self.bio = bio
        self.password = password


class Pitch(db.Model):

    # def __init__(self, title, description, cohort, github_link):

        # self.title = title
        # self.description = title
        # self.cohort = title
        # self.github_link
    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    github_link = db.Column(db.String)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

   

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(id=id).first()

        return pitches

    def __repr__(self):
        return f"Pitch {self.pitch}','{self.date}')"


class Comment():

    def __init__(self, description, pitch_id):

        self.description = description
        self.pitch_id = pitch_id
