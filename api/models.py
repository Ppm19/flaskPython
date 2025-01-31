from marshmallow import Schema, fields
class AlumnoSchema(Schema):
    id = fields.Str(dump_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    telefono = fields.Str(required=True)
class AlumnosSchema(Schema):
    id = fields.Str(dump_only=True)
    nombre = fields.Str()
    apellido = fields.Str()
    telefono = fields.Str()

alumno_schema = AlumnoSchema()
alumnos_schema = AlumnosSchema(many=True)

