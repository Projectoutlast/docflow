from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewTask(FlaskForm):

    '''Form for create a new task'''

    title = StringField(validators=[DataRequired()])
    describe = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Создать')
