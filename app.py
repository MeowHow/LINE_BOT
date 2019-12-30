from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from msglist import *
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Qkp+EE0efJEW32UpnhR7pnTvmq+aNaOLAcMn55zQvPDA9En2XbHmhBw37EDwa8R2Zbix6az4bkFl/6/feBhXSlWd6hqlSde7ezGvHodKBlXE121dQZdLlCRdPSFb6bX0Y2LSoZRz7vnfW29gdgDgbAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('759e2ef2de186697ffdcaf35f4bbafd4')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '店家' in msg or '哪裡買' in msg:
        message = msglist_Store()
        line_bot_api.reply_message(event.reply_token, message)
    elif '選單' in msg:
        message = msglist_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '產品示意圖' in msg:
        message = msglist_Product()
        line_bot_api.reply_message(event.reply_token, message)
    elif '餐廳' in msg:
        message = msglist_Recipe()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        #message = TextSendMessage(text=msg)
        message = replay_msglist(msg)
        line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
