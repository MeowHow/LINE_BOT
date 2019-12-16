from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def replay_msglist(msg):
    if '你好' in msg:
        return TextSendMessage(text="你好")
    elif '馬告' in msg and '功效' in msg:
        return TextSendMessage(text="馬告具有安眠、鎮痛與抗憂的功效喲～")
    elif msg == "幹":
    return TextSendMessage(text="幹三小？")



