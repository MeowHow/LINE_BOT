from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def replay_msglist(T):
    if '你好' in T:
        msg = TextSendMessage(text="你好")
        return msg
    elif '馬告' in T and '功效' in T:
        msg = TextSendMessage(text="馬告具有安眠、鎮痛與抗憂的功效喲～")
        return msg
    elif T == "幹":
        msg = TextSendMessage(text="幹三小？")
        return msg



