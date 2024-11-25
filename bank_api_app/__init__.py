
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    DB_NAME = 'banking.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from .api_views import api_views
    from .template_views import template_views
    from .models import db
    
    db.init_app(app)

    app.config['SECRET_KEY'] = "keepthisasecret"
    app.register_blueprint(template_views)
    app.register_blueprint(api_views)
    
    return app
