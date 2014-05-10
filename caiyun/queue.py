# -*- coding: utf-8 -*-

import requests
from flask import current_app
from flask.ext.rq import job
from .utils import caiyun_reply
from .sender import send_text
from settings import WEIXIN_TOKEN, CAIYUN_API, CAIYUN_TOKEN


@job
def reply_location(receiver, sender, x, y):
    url = CAIYUN_API.format(latitude=x,
                            longitude=y,
                            format='json',
                            product='minutes_prec_only',
                            token=CAIYUN_TOKEN)
    r = requests.get(url)
    data = r.json()
    content = caiyun_reply(data)
    send_text(receiver, content, WEIXIN_TOKEN)

def reply_location_sync(receiver, sender, x, y):
    url = CAIYUN_API.format(latitude=x,
                            longitude=y,
                            format='json',
                            product='minutes_prec',
                            token=CAIYUN_TOKEN)
    r = requests.get(url)
    data = r.json()
    content = caiyun_reply(data)
    return content
