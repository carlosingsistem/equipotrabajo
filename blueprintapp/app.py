from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from blueprintapp.extensions import db, login_manager
from blueprintapp.auth.models import User
# db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_equipo.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object("blueprintapp.config.Config")

    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))   
     
    # 1. Importación del blueprint (Para cada modulo)
    from blueprintapp.miembros import bp_miembro
    from blueprintapp.core import bp_core
    from blueprintapp.tareas import bp_tarea
    from blueprintapp.auth import auth_bp
    
    # 2. Registrar el blueprint (Para cada modulo)
    app.register_blueprint(bp_miembro)
    app.register_blueprint(bp_core)
    app.register_blueprint(bp_tarea)
    app.register_blueprint(auth_bp)
    
    return app