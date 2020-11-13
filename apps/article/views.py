from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from sqlalchemy import desc
from sqlalchemy.orm import load_only

from apps import redis_client
from models.article import Channel, Article
from datetime import datetime


class ChannelList(Resource):
    """
    频道管理
    """

    def get(self):
        channels = Channel.query.order_by('id').all()
        channel_list = []
        for channel in channels:
            channel_list.append(channel.to_dict())
        return channel_list


class ArticleResource(Resource):
    """
    文章管理
    """

    def get(self):
        rp = RequestParser()

        rp.add_argument('timestamp', required=True, location='args', type=int)

        args = rp.parse_args()
        timestamp = args.timestamp
        time = datetime.fromtimestamp(timestamp)
        articles = Article.query.options(
            load_only(Article.id, Article.title, Article.text, Article.cover, Article.ctime)). \
            filter(Article.is_delete == False, Article.ctime < time). \
            order_by(desc('ctime')).limit(10).all()
        article_list = []

        for article in articles:
            article_dict = {
                'id': article.id,
                'title': article.title,
                'text': article.text[:70],
                'cover': article.cover,
                'timestamp': int(datetime.timestamp(article.ctime))
            }

            article_list.append(article_dict)
        try:
            timestamp = int(datetime.timestamp(articles[-1].ctime))
        except:
            timestamp = timestamp
        return {
            'timestamp': timestamp,
            'article_list': article_list
        }


class ArticleInfoResource(Resource):
    def get(self, aid):
        article = Article.query.options(
            load_only(Article.id, Article.title, Article.ctime, Article.comment_count, Article.text)). \
            filter(Article.id == aid, Article.is_delete == False).first()

        key = f'article_click_{article.id}'

        click_count = redis_client.get(key)
        if not click_count:
            redis_client.set(key, 1)
            click_count = 1
        else:
            click_count = int(click_count) + 1
            redis_client.set(key, click_count)

        article_dict = {
            'id': article.id,
            'title': article.title,
            'ctime': article.ctime.strftime('%Y-%m-%d'),
            'comment_count': click_count,
            'text': article.text
        }
        return article_dict
