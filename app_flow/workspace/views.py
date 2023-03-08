from flask import flash, redirect, url_for
from flask_login import login_required, current_user
from flask import Blueprint, render_template

from app_flow.workspace.form import NewTask


blueprint = Blueprint('workplace', __name__, url_prefix='/workplace')


@blueprint.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    if current_user.is_authenticated:
        return render_template('base_workspace.html',
                               name=current_user.first_name)
    else:
        flash('Страница доступна аутентифицированным пользователям')
        return redirect(url_for('auth.login'))


@blueprint.route('/new', methods=['GET'])
@login_required
def create_new_task():
    form = NewTask()
    title = 'Новая задача'
    return render_template('tasks/create_task.html', form=form, title=title)
