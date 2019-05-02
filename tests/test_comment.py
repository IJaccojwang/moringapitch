import unittest
from app.models import Pitch,Comment
from app import db
from datetime import datetime

class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(title='New Pitch', description='This is the content',owners='people', cohort='mc4',technologies='python',comments='comments here',stars=4, pitched_p=datetime.now())
        self.new_comment = Comment(comment='This is my Test comment',pitch=new_pitch,pitched_c='here it is',user_c='us')

    def tearDown(self):
        db.session.delete(self.new_pitch)
        db.session.commit()
        db.session.delete(self.new_comment)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.name,'Test Comment')
        self.assertEquals(self.new_comment.comment, 'This is my Test comment')
        self.assertEquals(self.new_comment.pitched_c, 'here it is')
        self.assertEquals(self.new_comment.user_c, 'us')
        self.assertEquals(self.new_comment.pitch, new_pitch)