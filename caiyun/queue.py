# -*- coding: utf-8 -*-

import requests
from flask import current_app
from flask.ext.rq import job
from .utils import caiyun_reply
from .sender import send_text


@job
def reply_location(receiver, sender, x, y):
    WEIXIN_TOKEN = current_app.config['WEIXIN_TOKEN']
    CAIYUN_API = current_app.config['CAIYUN_API']
    CAIYUN_TOKEN = current_app.config['CAIYUN_TOKEN']

    url = CAIYUN_API.format(latitude=x,
                            longitude=y,
                            format='json',
                            product='minutes_prec',
                            token=CAIYUN_TOKEN)
    r = requests.get(url)
    data = r.json()
    content = caiyun_reply(data)
    send_text(receiver, content, WEIXIN_TOKEN)
