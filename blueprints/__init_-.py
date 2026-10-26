from blueprints.alumnos.routes import alumnos_bp
from blueprints.alumnos.routes import alumnos_bp

def registra_blueprints(app):
    app.register_blueprint(alumnos_bp)
    app.register_blueprint(maestros_bp)