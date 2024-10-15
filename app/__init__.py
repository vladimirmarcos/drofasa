from flask import Flask,render_template
#from flask_login import LoginManager
#from flask_sqlalchemy import SQLAlchemy
import os
import logging
from logging.handlers import SMTPHandler
#login_manager = LoginManager()
#db = SQLAlchemy()

   
def create_app(settings_module):
    """_summary_:función principal

    Args:
        settings_module (configuracion): _este argumento te dice como va a trabajar la app_

    Returns:
        _type_: _description_
    """
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(settings_module)
    #app.config["MODEL_FOLDER"]="app/static/models/" 
    #app.config["UPLOAD_FOLDER"]="app/static/"
    # Load the configuration from the instance folder
    #if app.config.get('TESTING', False):
     #   app.config.from_pyfile('config-testing.py', silent=True)
    #else:
     #   app.config.from_pyfile('config.py', silent=True)
    
    
    
    #login_manager.init_app(app)
    

    #db.init_app(app)
    
    #print(os.getenv('APP_SETTINGS_MODULE'))
    #print (f"el seting es {settings_module}")

    # Registro de los Blueprints
    """ 
    from .public import public_bp
    app.register_blueprint(public_bp)

    from .user import user_bp
    app.register_blueprint(user_bp)

    from .servicios import servicios_bp
    app.register_blueprint(servicios_bp)

    

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    register_error_handlers(app)"""
    return app