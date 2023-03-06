from flask import flash, redirect, url_for
from flask_login import login_required, login_manager, current_user
from flask import Blueprint, render_template


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


@blueprint.route('/tasks', methods=['GET'])
@login_required
def tasks():
    return render_template('tasks.html')
