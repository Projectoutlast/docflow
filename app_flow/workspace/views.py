from flask import Blueprint, render_template


blueprint = Blueprint('work', __name__)


@blueprint.route('/space', methods=['POST', 'GET'])
def space():
    return render_template('base_workspace.html')
