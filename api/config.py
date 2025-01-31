from pymongo import MongoClient
from marshmallow import Schema, fields

MONGO_URI = "mongodb+srv://ppermis:hola123@backvercel.n3fru.mongodb.net/?retryWrites=true&w=majority&appName=backVercel"
client = MongoClient(MONGO_URI)
db = client["robertExpress"]

class AlumnoSchema(Schema):
    id = fields.Str()
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    telefono = fields.Str(required=True)

alumno_schema = AlumnoSchema()
alumnos_schema = AlumnoSchema(many=True)