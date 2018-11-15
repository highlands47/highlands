from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class RegistrationForm(
    FlaskForm):  # instead of inheriting from (Model) as taught in Treehouse, I inherited from FlaskForm
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=10)])
