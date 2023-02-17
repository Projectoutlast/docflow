from flask import Flask, render_template

from app_flow.db import db
from app_flow.schema_db import Company, Employee
from app_flow.register.views import blueprint as reg_blueprint


def create_app():

    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(reg_blueprint)

    @app.route('/')
    def index():
        title = 'Главная страница'
        return render_template('index.html', title=title)

    return app
