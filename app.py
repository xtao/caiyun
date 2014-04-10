import requests
from flask import Flask
from flask_weixin import Weixin
from caiyun import settings

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
        s = data.get('status')
        if s == 'ok':
            content = data.get('summary', '')
        else:
            content = r.text
        return weixin.reply(username,
                            sender=sender,
                            content=content)
    return weixin.reply(username,
                        sender=sender,
                        content=content)


if __name__ == "__main__":
    app.run()
