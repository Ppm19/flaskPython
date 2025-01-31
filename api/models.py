from marshmallow import Schema, fields, ValidationError
from bson import ObjectId

def validate_objectid(value):
    try:
        return ObjectId(value)
    except:
        raise ValidationError("ID inválido.")

class UserSchema(Schema):
    _id = fields.Str(validate=validate_objectid, dump_only=True)
    name = fields.Str(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
