from flask import Flask



def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'hjshjhdjdfghjkah kjshkjdhjs'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app