# -*- coding: utf-8 -*-

from flask import Flask
from flask_weixin import Weixin
from flask.ext.rq import RQ
from caiyun import settings
from caiyun.queue import reply_location

app = Flask(__name__)
app.config.from_object(settings)

weixin = Weixin()
weixin.init_app(app)
app.add_url_rule('/', view_func=weixin.view_func)

RQ(app)

CAIYUN_API = app.config['CAIYUN_API']
CAIYUN_TOKEN = app.config['CAIYUN_TOKEN']

DEFAULT_MSG = u'主页君对您的文字表示理解不能……点击底部输入栏右侧的加号，然后选择位置，主页君才可以为您报天气呢。'
SUBSCRIBE_MSG = u'感谢您关注彩云天气的微信公众号！' \
    u'点击底部输入栏右侧的加号，然后选择位置，即可为您预报未来一小时几点几分下雨，现在就试试吧！'


@weixin.register('*')
def reply(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    content = kwargs.get('content')
    content = DEFAULT_MSG
    type = kwargs.get('type')
    if type == 'location':
        x = kwargs.get('location_x')
        y = kwargs.get('location_y')
        reply_location.delay(username, sender, x, y)
        content = u'您的地址已收到，彩云天气正在分析您当地的天气情况。'
        return weixin.reply(username,
                            sender=sender,
                            content=content)
    elif type == 'event':
        event = kwargs.get('event')
        if event == 'subscribe':
            content = SUBSCRIBE_MSG
    return weixin.reply(username,
                        sender=sender,
                        content=content)


if __name__ == "__main__":
    app.run()
