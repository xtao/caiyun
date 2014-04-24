# -*- coding: utf-8 -*-

import json
import requests

SENDER_API = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s"


def send_text(to_user=None, content=None, token=None):
    data = {
        'touser': to_user,
        'msgtype': 'text',
        'text': {'content': content},
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(SENDER_API % token,
                  data=json.dumps(data),
                  headers=headers)
