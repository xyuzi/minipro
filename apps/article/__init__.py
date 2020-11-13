from flask import Blueprint
from flask_restful import Api

home_bp = Blueprint('article', __name__)

api = Api(home_bp)
from .views import *

api.add_resource(ChannelList, '/articles/Channel_list/')
api.add_resource(ArticleResource, '/articles/')
api.add_resource(ArticleInfoResource, '/articles/<int:aid>/')
