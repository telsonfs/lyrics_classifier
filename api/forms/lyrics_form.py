from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class LyricForm(FlaskForm):
    lyric = TextAreaField('lyric', validators=[DataRequired()])