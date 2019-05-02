from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email, Length


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    owners = TextAreaField('Owners/Members', validators=[Required()])
    cohort = StringField('Cohort', validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[Required()])
    submit = SubmitField('Submit')