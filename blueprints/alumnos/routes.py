from flask import Blueprint, jsonify, request
from database import mysql


alumnos_bp = Blueprint(
    'alumnos',          # <-- ¡Aquí faltaba la coma!
    __name__,
    url_prefix='/api/alumnos'
)
 
def fila_a_diccionario(cursor, fila):
    columnas = [columna[0] for columna in cursor.descripcion]
    return dict(zip(columnas, fila))
 
@alumnos_bp.route("/", methods=['GET'])
def listar_alumnos():
    cursor = None
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT * FROM alumnos
            """
        )
        datos = cursor.fetchall()
        alumnos = [
            fila_a_diccionario(cursor, fila)
            for fila in datos
        ]
        return jsonify({
            'alumnos': alumnos,
            'mensaje': "Lista de alumnos",
            'exito': True  # Lo cambié a True ya que la consulta fue exitosa
        }), 200  # El código de estado HTTP va separado por coma fuera del diccionario
       
    except Exception as ex:
        return jsonify({
            'mensaje': f"Error al listar alumnos: {str(ex)}",
            'exito': False
        }), 500  # Código 500 de error en el servidor
       
    finally:
        if cursor is not None:
            cursor.close()
 