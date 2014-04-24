# -*- coding: utf-8 -*-

WEIXIN_TOKEN = ""
WEIXIN_SENDER = ""
WEIXIN_EXPIRES_IN = ""

CAIYUN_TOKEN = ""
CAIYUN_API = "%s?%s" % ("http://rain.swarma.net/fcgi-bin/v1/api.py",
                        "lonlat={longitude},{latitude}"
                        "&format={format}"
                        "&product={product}"
                        "&token={token}")

RQ_DEFAULT_HOST = 'localhost'
RQ_DEFAULT_PORT = 6479
RQ_DEFAULT_PASSWORD = ""
RQ_DEFAULT_DB = 1

try:
    from local_settings import *
except ImportError:
    pass
