from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email, Length


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    text = TextAreaField('Description', validators=[Required()])
    category = SelectField('github', validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[Required()])
    submit = SubmitField('Submit')