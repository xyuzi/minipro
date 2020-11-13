from datetime import datetime

from sqlalchemy.dialects.mysql import DATETIME

from apps import db


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True, doc='频道ID')
    name = db.Column(db.String(20), unique=True, doc='频道名称')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, doc='文章ID')
    user_id = db.Column(db.Integer, doc='用户ID')
    channel_id = db.Column(db.Integer, doc='频道ID')
    title = db.Column(db.String(130), doc='标题')
    cover = db.Column(db.String(130), doc='封面')
    ctime = db.Column(DATETIME(fsp=3), default=datetime.now, doc='创建时间')
    comment_count = db.Column(db.Integer, default=0, doc='评论数')
    text = db.Column(db.TEXT, doc='文章内容')
    is_delete = db.Column(db.Boolean, default=0, doc='逻辑删除')
