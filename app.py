from flask import Flask
from flask_weixin import Weixin
from caiyun import settings

app = Flask(__name__)
app.config.from_object(settings)

weixin = Weixin()
weixin.init_app(app)
app.add_url_rule('/', view_func=weixin.view_func)


@weixin.register('*')
def reply(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    content = kwargs.get('content')
    return weixin.reply(username,
                        sender=sender,
                        content=content)


if __name__ == "__main__":
    app.run()
