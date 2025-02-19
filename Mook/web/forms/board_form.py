from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import DataRequired

class BoardForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired("Please Enter Title.")])
    writer = StringField('Writer', validators=[DataRequired("Please Login.")])
    content = TextAreaField('Content', validators=[DataRequired("Please Enter Content.")])