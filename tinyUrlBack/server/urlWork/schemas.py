from marshmallow import Schema, fields


class longToShortUrlSchema(Schema):
    longUrl = fields.Str(required=True)
    shortUrl = fields.Str(dump_only=True)
    shortUrlId = fields.Str(dump_only=True)

class redirectUrlSchema(Schema):
    longUrl = fields.Str(dump_only=True)
    