from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class ReviewForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    review = TextAreaField('Review', validators=[DataRequired(), Length(1, 300)])
    mark = StringField('Mark', validators=[DataRequired(), Length(1,5)])
    submit = SubmitField()