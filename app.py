from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

#創造 Flask 物件
app = Flask(__name__)

line_bot_api = LineBotApi('Y+JbSeJypNx26Ek5Irscb/hrLQs6iAjDx/KVGHvtcsqtFAzhvmlsu6jJagY337gvJr5UUcCR94OTdUh3ltQF8whc4X4ouQSUdGd8t2rOrw/kUpjM8nX7Lq9gzboefgODN/2aCYFL790eWoA6pkbEQQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('Ue206e9dcc98e25dc0bba3e4783cd9ba2')

#監聽Line的POST請求，並給handler進行處裡
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
