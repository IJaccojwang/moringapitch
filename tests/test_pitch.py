import unittest
from app.models import Pitch
from app import db
from datetime import datetime

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(title='New Pitch', description='This is the content',owners='people', cohort='mc4',technologies='python',comments='comments here',stars=4, pitched_p=datetime.now())

    def tearDown(self):
        db.session.delete(self.new_pitch)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title,'New Pitch')
        self.assertEquals(self.new_pitch.description,'This is the content')
        self.assertEquals(self.new_pitch.owners, 'people')
        self.assertEquals(self.new_pitch.cohort, 'mc4')
        self.assertEquals(self.new_pitch.technologies, 'python')
        self.assertEquals(self.new_pitch.comments, 'comments here')
        self.assertEquals(self.new_pitch.stars,4)
      


    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        pitch = Pitch.get_pitch()
        self.assertTrue(pitch is not None)