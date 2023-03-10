from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class CompanyRegister(FlaskForm):

    '''Form for register a company'''

    type_company = StringField(
        'Введите форму собственности', validators=[
            DataRequired(), Length(max=20)])
    company_name = StringField(
        'Введите наименование компании', validators=[
            DataRequired(), Length(max=50)])
    email = StringField(
        'Введите электронную почту', validators=[
            DataRequired(), Email()])
    tax_identification_number = IntegerField(
        'Введите ИНН компании', validators=[DataRequired()])
    password = PasswordField(
        'Введите пароль', validators=[
            DataRequired(), EqualTo(
                'password2', message='Пароли не совпадают')])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class EmployeeRegister(FlaskForm):

    '''Form for register a employee'''

    last_name = StringField(
        'Введите Вашу фамилию', validators=[DataRequired(), Length(max=30)])
    first_name = StringField(
        'Введите Ваше имя', validators=[DataRequired(), Length(max=30)])
    patronymic = StringField(
        'Введите Ваше отчество', validators=[DataRequired(), Length(max=30)])
    email = StringField(
        'Введите Вашу электронную почту', validators=[
            DataRequired(), Length(max=30)])
    tax_identification_number = IntegerField(
        'Введите ИНН компании', validators=[DataRequired()])
    password = PasswordField(
        'Введите пароль', validators=[
            DataRequired(), EqualTo(
                'password2', message='Пароли не совпадают')])
    password2 = PasswordField('Повторите пароль')
    submit = SubmitField('Зарегистрироваться')
