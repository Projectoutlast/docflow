from flask import Flask, render_template
from flask_login import LoginManager

from app_flow.db import db
from app_flow.schema_db import Company, Employee
from app_flow.register.views import blueprint as reg_blueprint
from app_flow.athentication.views import blueprint as auth_blueprint
from app_flow.workspace.views import blueprint as work_blueprint
from app_flow.workspace.queries import blueprint as query_blueprint


def create_app():

    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def employee_load(employee_id):
        return Employee.query.get(int(employee_id))

    app.config.from_pyfile('config.py')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(reg_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(work_blueprint)
    app.register_blueprint(query_blueprint)

    @app.route('/')
    def index():
        title = 'Главная страница'
        return render_template('index.html', title=title)

    return app
