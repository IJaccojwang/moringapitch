from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email, Length


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    owners = TextAreaField('Owners/Members', validators=[Required()])
    technologies = TextAreaField('Technologies used', validators=[Required()])
    cohort = SelectField('Select cohort', choices=[('mc1', 'MC1'),('mc2', 'MC2'),('mc3', 'MC3'),('mc4', 'MC4'),('mc5', 'MC5'),('mc6', 'MC6'),('mc7', 'MC7'),('mc8', 'MC8'),('mc9', 'MC9'),('mc10', 'MC10'),('mc11', 'MC11'),('mc12', 'MC12'),('mc13', 'MC13'),('mc14', 'MC14'),('mc15', 'MC15')])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[Required()])
    submit = SubmitField('Submit')