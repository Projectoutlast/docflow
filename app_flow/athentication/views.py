from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_required, logout_user, login_user
from werkzeug.security import check_password_hash

from app_flow.athentication.forms import EmployeeLogin
from app_flow.schema_db import Employee


blueprint = Blueprint('auth', __name__)


@blueprint.route('/login', methods=['POST', 'GET'])
def login():

    '''Page for authentication'''

    form = EmployeeLogin()
    title = 'Вход'
    return render_template('login_page.html', form=form, title=title)


@blueprint.route('/login-post', methods=['POST'])
def login_post():

    '''Process for authentication'''

    form = EmployeeLogin()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = True if form.remember.data else False

        user = Employee.query.filter_by(employee_email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=remember)
            return redirect(url_for('workplace.home'))
        else:
            flash('Неверные почта или пароль')
            return redirect(url_for('auth.login'))


@blueprint.route('/logout')
@login_required
def logout():

    '''Process for logout'''

    logout_user()
    return redirect(url_for('auth.login'))
