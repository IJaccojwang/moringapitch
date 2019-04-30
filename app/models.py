from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import admin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self, author, quote):
        self.author = author
        self.quote = quote


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    stars = db.relationship('Star', backref='pitch', lazy='dynamic')
    pitched_p = db.Column(db.DateTime,default=datetime.utcnow)
    user_p = db.Column(db.Integer,db.ForeignKey("users.id"),  nullable=False)
    

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Post.query.order_by(pitch_id=id).desc().all()
        return pitches

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    pitched_c = db.Column(db.DateTime,default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"), nullable=False)
    user_c = db.Column(db.Integer,db.ForeignKey("users.id"), nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(pitch_id=id).all()
        return comments



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitch = db.relationship('Post', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    stars = db.relationship('Star', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Star(db.Model):
    __tablename__ = 'stars'

    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.Integer, default=1)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_stars(self):
        db.session.add(self)
        db.session.commit()

    def add_stars(cls, id):
        star_pitch = Star(user=current_user, pitch_id=id)
        star_pitch.save_stars()

    @classmethod
    def get_stars(cls, id):
        star = Star.query.filter_by(pitch_id=id).all()
        return star

    @classmethod
    def get_all_stars(cls, pitchh_id):
        stars = Star.query.order_by('id').all()
        return stars

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
