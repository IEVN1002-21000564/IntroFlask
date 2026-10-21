from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS 

from config import config

app = Flask(__name__)

# Es importante cargar la configuración ANTES de inicializar extensiones como MySQL
app.config.from_object(config['development'])

CORS(app)
con = MySQL(app)

@app.route("/alumnos", methods=['GET'])
def lista_alumnos():
    try:
        cursor = con.connection.cursor()
        sql = "select * from alumnos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumno = {
                "matricula": fila[0],
                "nombre": fila[1],
                "apaterno": fila[2],
                "amaterno": fila[3],
                "correo": fila[4]
            }
            alumnos.append(alumno)
        return jsonify({
            'alumnos': alumnos,
            'mensaje': 'Lista de alumnos',
            'exito': True
        })
    except Exception as ex:
        return jsonify({
            "message": f"error {ex}",
            'exito': False
        })

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>", 404

# Registrar el manejador de errores correctamente
app.register_error_handler(404, pagina_no_encontrada)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)