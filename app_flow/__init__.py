from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Главная страница'
        return render_template('base.html')
    
    return app
