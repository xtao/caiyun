# -*- coding: utf-8 -*-

import requests
from flask import Flask
from flask_weixin import Weixin
from caiyun import settings
from caiyun.utils import caiyun_reply

app = Flask(__name__)
app.config.from_object(settings)

weixin = Weixin()
weixin.init_app(app)
app.add_url_rule('/', view_func=weixin.view_func)

CAIYUN_API = app.config['CAIYUN_API']
CAIYUN_TOKEN = app.config['CAIYUN_TOKEN']


@weixin.register('*')
def reply(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    content = kwargs.get('content')
    type = kwargs.get('type')
    if type == 'location':
        x = kwargs.get('location_x')
        y = kwargs.get('location_y')
        url = CAIYUN_API.format(latitude=x,
                                longitude=y,
                                format='json',
                                product='minutes_prec',
                                token=CAIYUN_TOKEN)
        r = requests.get(url)
        data = r.json()
        content = caiyun_reply(data)
        return weixin.reply(username,
                            sender=sender,
                            content=content)
    content = u"请发送微信位置过来，感谢。"
    return weixin.reply(username,
                        sender=sender,
                        content=content)


if __name__ == "__main__":
    app.run()
