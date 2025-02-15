from flask import Flask, jsonify, request
from flask_cors import CORS
from api.config import db
from api.models import alumno_schema, alumnos_schema

app = Flask(__name__)
CORS(app, origins="https://vercel-front-sage.vercel.app")

alumnos_collection = db["alumnos"]


@app.route('/api/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = list(alumnos_collection.find({}, {"_id": 0, "id": 1, "nombre": 1, "apellido": 1, "telefono": 1}))
    return jsonify(alumnos_schema.dump(alumnos))


@app.route('/api/alumnos/<alumno_id>', methods=['GET'])
def get_alumno_by_id(alumno_id):
    try:
        print(f"Buscando alumno con id: {alumno_id}")
        alumno = alumnos_collection.find_one({"id": str(alumno_id)})

        if not alumno:
            return jsonify({"error": "Alumno no encontrado"}), 404

        return jsonify(alumno_schema.dump(alumno))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/alumnos', methods=['POST'])
def add_alumno():
    try:
        data = request.get_json()

        if not all(k in data for k in ("nombre", "apellido", "telefono", "id")):
            return jsonify({"error": "Todos los campos son necesarios."}), 400

        if alumnos_collection.find_one({"id": data["id"]}):
            return jsonify({"error": f"Ya existe un alumno con el id {data['id']}."}), 409

        result = alumnos_collection.insert_one({
            "id": str(data["id"]),
            "nombre": data["nombre"],
            "apellido": data["apellido"],
            "telefono": data["telefono"]
        })

        return jsonify(data), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
