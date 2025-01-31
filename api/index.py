from flask import Flask, jsonify, request
from flask_cors import CORS
from bson import ObjectId
from API.config import db
from API.models import user_schema, users_schema

app = Flask(__name__)
CORS(app)
users_collection = db["users"]

# Obtener todos los usuarios
@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {"_id": 1, "name": 1}))
    return jsonify(users_schema.dump(users))

# Obtener usuario por ID
@app.route('/api/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404
        return jsonify(user_schema.dump(user))
    except:
        return jsonify({"error": "ID inválido"}), 400

# Agregar un usuario
@app.route('/api/users', methods=['POST'])
def add_user():
    try:
        data = user_schema.load(request.get_json())
        result = users_collection.insert_one({"name": data["name"]})
        data["_id"] = str(result.inserted_id)
        return jsonify(data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400