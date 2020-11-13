from apps import db


class User(db.Model):
    """
    用户基本信息
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, doc='用户ID')
    mobile = db.Column(db.String(11), doc='手机号')
    name = db.Column(db.String(20), doc='昵称')
    last_login = db.Column(db.DateTime, doc='最后登录时间')
    article_count = db.Column(db.Integer, default=0, doc='作品数')
    profile_photo = db.Column(db.String(130), doc='头像')

    def to_dict(self):
        """模型转字典, 用于序列化处理"""

        return {
            'id': self.id,
            'name': self.name,
            'photo': self.profile_photo,
        }