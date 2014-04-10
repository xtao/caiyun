WEIXIN_TOKEN = ""
WEIXIN_SENDER = ""
WEIXIN_EXPIRES_IN = ""

CAIYUN_TOKEN = ""
CAIYUN_API = "%s?%s" % ("http://rain.swarma.net/fcgi-bin/v1/api.py",
                        "lonlat={longitude},{latitude}"
                        "&format={format}"
                        "&product={product}"
                        "&token={token}")

try:
    from local_settings import *
except ImportError:
    pass
