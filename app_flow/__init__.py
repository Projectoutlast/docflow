from flask import Flask, render_template

from app_flow.register.views import blueprint as reg_blueprint


def create_app():

    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    app.register_blueprint(reg_blueprint)

    @app.route('/')
    def index():
        title = 'Главная страница'
        return render_template('base.html', title=title)

    return app
