from flask import Flask, jsonify, request
from flask_cors import CORS
from bson import ObjectId
from api.config import db
from models import alumno_schema, alumnos_schema

app = Flask(__name__)
CORS(app, origins="https://vercel-front-sage.vercel.app")

alumnos_collection = db["alumnos"]


@app.route('/api/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = list(alumnos_collection.find({}, {"_id": 1, "nombre": 1, "apellido": 1, "telefono": 1}))
    return jsonify(alumnos_schema.dump(alumnos))


@app.route('/api/alumnos/<alumno_id>', methods=['GET'])
def get_alumno_by_id(alumno_id):
    try:
        alumno = alumnos_collection.find_one({"_id": ObjectId(alumno_id)})
        if not alumno:
            return jsonify({"error": "Alumno no encontrado"}), 404
        return jsonify(alumno_schema.dump(alumno))
    except:
        return jsonify({"error": "ID inválido"}), 400

@app.route('/api/alumnos', methods=['POST'])
def add_alumno():
    try:
        data = alumno_schema.load(request.get_json())
        result = alumnos_collection.insert_one({
            "nombre": data["nombre"],
            "apellido": data["apellido"],
            "telefono": data["telefono"]
        })
        
        data["_id"] = str(result.inserted_id)
        return jsonify(data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

if __name__ == '__main__':
    app.run()
