# -*- coding: utf-8 -*-

import requests
from flask.ext.rq import job
from .utils import (caiyun_reply,
                    caiyun_coord_reply,
                    caiyun_coord_text_reply)
from .sender import send_text
from settings import (WEIXIN_TOKEN,
                      CAIYUN_API,
                      CAIYUN_TOKEN,
                      CAIYUN_COORD_API,
                      CAIYUN_COORD_TEXT_API)
MSG = u"{address}: {summary}"

MSG1 = u"{summary} (访问 http://caiyunapp.com/#{longitude},{latitude} 查看详情)"




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
    return MSG1.format(summary=content,
                       longitude=y,
					   latitude=x)


def reply_text_sync(receiver, sender, text, default):
    url = CAIYUN_COORD_API.format(address=text)
    r = requests.get(url)
    data = r.json()
    lat, lon = caiyun_coord_reply(data)
    if not all([lat, lon]):
        return default
    url = CAIYUN_COORD_TEXT_API.format(longitude=lon,
                                       latitude=lat)
    r = requests.get(url)
    data = r.json()
    address = caiyun_coord_text_reply(data)
    if not address:
		address = text
    summary = reply_location_sync(receiver, sender, lat, lon)
    if not summary:
        return default
    return MSG.format(address=address,
                      summary=summary)
