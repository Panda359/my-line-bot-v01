from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

from linepy import *

app = Flask(__name__)

cl = LINE("fSTr2G4/t3EQ2vocVfa7xSRDUWDJVkKtPYFOTfQOhSE+H4XS9iir2Scv/jjqNAl4OC3fZlgTSHPvEAv0SC49WkhLza2J3qWAWJ5BotlBD1brgoCWAjJT4KGZDNeABUBMHgcn68Ofb+t7srQviEYjOgdB04t89/1O/w1cDnyilFU=")
#cl = LINE("TOKENMU")
#cl = LINE("Email","Password")
#cl = LINE()
cl.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
cl.log("Channel Token : " + str(channelToken))

line_bot_api = LineBotApi('fSTr2G4/t3EQ2vocVfa7xSRDUWDJVkKtPYFOTfQOhSE+H4XS9iir2Scv/jjqNAl4OC3fZlgTSHPvEAv0SC49WkhLza2J3qWAWJ5BotlBD1brgoCWAjJT4KGZDNeABUBMHgcn68Ofb+t7srQviEYjOgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('91aba13ad024feeb462ae8ae2a72a7ba')





@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
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
