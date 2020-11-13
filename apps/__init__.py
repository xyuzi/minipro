from flask import Flask
from flask_migrate import Migrate

from settings import config_dict
from utils.constants import EXTRA_ENV_COINFIG
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

db = SQLAlchemy()
redis_client = None  # type: StrictRedis


def register_extensions(app):
    """
    组件初始化
    :param app:
    :return:
    """
    db.init_app(app)
    global redis_client

    redis_client = StrictRedis(host=app.config['REDIS_HOST'],
                               port=app.config['REDIS_PORT'],
                               decode_responses=True)


def register_bp(app: Flask):
    """
    注册蓝图
    :param app:
    :return:
    """
    from apps.article import home_bp
    app.register_blueprint(home_bp)


def create_flask_app(project_type):
    """
    创建app
    :param type:
    :return:
    """
    app = Flask(__name__)

    conf_obj = config_dict[project_type]
    app.config.from_object(conf_obj)
    app.config.from_envvar(EXTRA_ENV_COINFIG, silent=True)

    Migrate(app, db)
    from models import article, user
    return app


def create_app(project_type):
    app = create_flask_app(project_type)
    register_extensions(app)
    register_bp(app)

    return app
