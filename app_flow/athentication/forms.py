from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class EmployeeLogin(FlaskForm):

    '''Form for log in'''

    email = StringField('Введите email', validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня', default=True)
    submit = SubmitField('Войти')
