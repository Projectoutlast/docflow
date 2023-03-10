from flask import flash
from flask_login import login_required
from flask import Blueprint, render_template

from app_flow.schema_db import Task


blueprint = Blueprint('queries', __name__, url_prefix='/queries')


@blueprint.route('/all-tasks', methods=['POST', 'GET'])
@login_required
def all_current_tasks():

    '''Get and show all current tasks'''

    get_all_tasks = Task.query.filter(Task.status == 1).all()
    list_of_tasks = [(task.title, task.describe) for task in get_all_tasks]
    return render_template('tasks/all_current_tasks.html', tasks=list_of_tasks)


def all_complete_tasks():

    '''Get and show all completed tasks'''

    pass
