from flask import Blueprint, flash, render_template, redirect, url_for

from app_flow.register.forms import CompanyRegister, EmployeeRegister
from app_flow.db import db
from app_flow.schema_db import Company, Employee


blueprint = Blueprint('register', __name__, url_prefix='/register')


@blueprint.route('/register-company', methods=['POST', 'GET'])
def register_company():

    '''Page of registration for company'''

    form = CompanyRegister()
    title = 'Регистрация компании'
    return render_template('reg_company.html', form=form, title=title)


@blueprint.route('/company-register-procces', methods=['POST', 'GET'])
def company_register_procces():

    '''Process registration for company'''

    form = CompanyRegister()
    if form.validate_on_submit():
        company_email = Company.query.filter_by(
                company_email=form.email.data
            ).first()
        tax_number = Company.query.filter_by(
            tax_identification_number=form.tax_identification_number.data
            ).first()

        if tax_number:
            flash('Компания с таким ИНН уже существует')
            return redirect(url_for('register.register_company'))

        if company_email:
            flash('Компания с таким email уже существует')
            return redirect(url_for('register.register_company'))

        new_company = Company(
            type_company=form.type_company.data,
            company_name=form.company_name.data,
            company_email=form.email.data,
            tax_identification_number=form.tax_identification_number.data
        )
        new_company.set_password(form.password.data)
        db.session.add(new_company)
        db.session.commit()
        flash('Компания успешно зарегистрирована')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('register.register_company'))


@blueprint.route('/register-employee', methods=['POST', 'GET'])
def register_employee():

    '''Page of registration for employee'''

    form = EmployeeRegister()
    title = 'Регистрация пользователя'
    return render_template('reg_employee.html', form=form, title=title)


@blueprint.route('/employee-register-procces', methods=['POST', 'GET'])
def employee_register_procces():

    '''Process registration for employee'''

    form = EmployeeRegister()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(
            employee_email=form.email.data).first()

        company_id = db.session.query(Company.id).filter_by(
            tax_identification_number=form.tax_identification_number.data
        ).first()

        if employee:
            flash('Пользователь с таким email уже зарегистрирован')
            return redirect(url_for('register.register_employee'))

        if not company_id:
            flash('Компания с таким ИНН не зарегистрирована')
            return redirect(url_for('register.register_employee'))

        new_employee = Employee(
            company_id=company_id[0],
            last_name=form.last_name.data,
            first_name=form.first_name.data,
            patronymic=form.patronymic.data,
            employee_email=form.email.data
        )
        new_employee.set_password(form.password.data)
        db.session.add(new_employee)
        db.session.commit()
        flash('Вы успешно зарегистрированы')
        return redirect(url_for('auth.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Error in field "{}" - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('register.register_employee'))
