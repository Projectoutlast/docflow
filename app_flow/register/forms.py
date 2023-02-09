from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class CompanyRegister(FlaskForm):
    company_name = StringField(
        'Введите наименование компании', validators=[
            DataRequired(), Length(max=50)])
    tax_identification_number = IntegerField(
        'Введите ИНН компании', validators=[DataRequired()])
    email = StringField(
        'Введите электронную почту', validators=[
            DataRequired(), Email()])
    password = PasswordField(
        'Введите пароль', validators=[
            DataRequired(), EqualTo(
                'password2', message='Пароли не совпадают')])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class EmployeeRegister(FlaskForm):
    username = StringField(
        'Введите Ваше имя', validators=[DataRequired(), Length(max=30)])
    surname = StringField(
        'Введите Вашу фамилию', validators=[DataRequired(), Length(max=30)])
    lastname = StringField(
        'Введите Ваше отчество', validators=[DataRequired(), Length(max=30)])
    email = StringField(
        'Введите Вашу электронную почту', validators=[
            DataRequired(), Length(max=30)])
    company_tax_identification_number = IntegerField(
        'Введите ИНН компании', validators=[DataRequired()])
    password = PasswordField(
        'Введите пароль', validators=[
            DataRequired(), EqualTo(
                'password2', message='Пароли не совпадают')])
    password2 = PasswordField('Повторите пароль')
    submit = SubmitField('Зарегистрироваться')
