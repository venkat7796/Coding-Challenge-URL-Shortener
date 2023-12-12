from flask import jsonify, make_response
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from schemas import longToShortUrlSchema, redirectUrlSchema
from db import db
from model.urlmap import urlModel
from urlconversion import create_mapping_fn

blp = Blueprint("tinyurl",__name__,description="Convert LongUrl to ShortUrl")
#table = create_session()

@blp.route("/api/v1/converturl")
class longToShortUrl(MethodView):
    @blp.arguments(longToShortUrlSchema)
    @blp.response(201,longToShortUrlSchema)
    def post(self,longurl_payload):
        longUrlTabResult = urlModel.query.filter(urlModel.longUrl == longurl_payload["longUrl"]).first()
        if longUrlTabResult:
            abort(400,message=f"Short Url {longUrlTabResult.shortUrl} is already created")
        else:
            tiny_url_suffix = create_mapping_fn()
            shortUrl = "http://localhost:5000" + "/" + tiny_url_suffix
            longUrlData = urlModel(longUrl = longurl_payload["longUrl"],
                                shortUrl = shortUrl,
                                shortUrlId = tiny_url_suffix)
            try:
                db.session.add(longUrlData)
                db.session.commit()
            except SQLAlchemyError:
                abort(400,message="Error while adding data to the database")
            return longUrlData

@blp.route("/<string:shortUrlId>")
class redirectUrl(MethodView):
    def get(self,shortUrlId):
        urlTabResult = urlModel.query.filter(urlModel.shortUrlId == shortUrlId).first()
        if not urlTabResult:
            abort(400,message="Redirect Url does not exist")
        print(urlTabResult.longUrl)
        return urlTabResult.longUrl, 302
    
    def delete(self,shortUrlId):
        urlTabResult = urlModel.query.filter(urlModel.shortUrlId == shortUrlId).first()
        if not urlTabResult:
            abort(400,message="ShortURL is already deleted or not found")
        try:
            db.session.delete(urlTabResult)
            db.session.commit()
        except SQLAlchemyError:
            abort(400,message="Error while deleting entry")
        return {"Message": "Short URL deleted successfully"}, 201
