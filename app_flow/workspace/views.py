from flask import flash, redirect, url_for
from flask_login import login_required, current_user
from flask import Blueprint, render_template

from app_flow.workspace.form import NewTask
from app_flow.schema_db import Task
from app_flow.db import db


blueprint = Blueprint('workplace', __name__, url_prefix='/workplace')


@blueprint.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    if current_user.is_authenticated:
        return render_template('base_workspace.html')
    else:
        flash('Страница доступна аутентифицированным пользователям')
        return redirect(url_for('auth.login'))


@blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def create_new_task():

    '''Page for creating a new task'''

    form = NewTask()
    title = 'Новая задача'
    return render_template('tasks/create_task.html', form=form, title=title)


@blueprint.route('/task-create-process', methods=['POST'])
@login_required
def task_create_process():

    '''Process for creating a new task'''

    form = NewTask()
    if form.validate_on_submit():
        user_id = current_user.id
        new_task = Task(
            employee_id=user_id,
            title=form.title.data,
            describe=form.describe.data)

        db.session.add(new_task)
        db.session.commit()

        flash('Задача успешно создана')
        return redirect(url_for('workplace.create_new_task'))
    else:
        flash(form.validate_on_submit())
        flash('Заполните корректно все поля')
        return redirect(url_for('workplace.create_new_task'))
