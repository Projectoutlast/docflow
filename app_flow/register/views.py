from flask import Blueprint, flash, render_template, redirect, url_for

from app_flow.register.forms import CompanyRegister, EmployeeRegister


blueprint = Blueprint('register', __name__, url_prefix='/register')


@blueprint.route('/company', methods=['POST', 'GET'])
def register_company():
    form = CompanyRegister()
    title = 'Регистрация компании'
    return render_template('reg_company.html', form=form, title=title)


@blueprint.route('/company-reg-procces', methods=['POST', 'GET'])
def company_register_procces():
    pass


@blueprint.route('/employee', methods=['POST', 'GET'])
def register_employee():
    form = EmployeeRegister()
    title = 'Регистрация пользователя'
    return render_template('reg_employee.html', form=form, title=title)


@blueprint.route('/employee-reg-procces', methods=['POST', 'GET'])
def employee_register_procces():
    pass
