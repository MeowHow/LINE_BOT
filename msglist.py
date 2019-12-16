from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def replay_msglist(msg):
    if '你好' in msg:
        ReMsg = '你好'
    return ReMsg 


