from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewTask(FlaskForm):
    title = StringField('Тема', validators=[DataRequired()])
    describe = TextAreaField('Описание', validators=[DataRequired()])
    submit = SubmitField('Создать')
