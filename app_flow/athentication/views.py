from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_required, logout_user, login_user

from app_flow.athentication.forms import EmployeeLogin
from app_flow.schema_db import Employee


blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/authentication', methods=['POST', 'GET'])
def authentication():

    '''Page authentication function'''

    form = EmployeeLogin()
    title = 'Вход'
    return render_template('login_page.html', form=form, title=title)


@blueprint.route('/process-authentication', methods=['POST'])
def process_authentication():

    '''Process authentication function'''

    form = EmployeeLogin()
    if form.validate_on_submit():
        user = Employee.query.filter_by(employee_email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('work.space'))
    else:
        flash('Неверные почта или пароль')
        return redirect(url_for('auth.authentication'))


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
