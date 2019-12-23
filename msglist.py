from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#關鍵字清單
def replay_msglist(T):
    if '你好' in T or 'Hi' in T or '早安' in T or '早上好' in T:
        msg = TextSendMessage(text="你好～這裡是瑪糕～\n可以問我問題唷，如果不知道要問甚麼可以輸入選單兩個字呼叫快問選單～")
        return msg
    elif '馬告' in T and '功效' in T:
        msg = TextSendMessage(text="馬告具有安眠、鎮痛與抗憂的功效喲～")
        return msg
    elif '馬告' in T and '產品' in T:
        msg = TextSendMessage(text="新鮮或乾燥的馬告都可以作為調味料使用！\n現在也有很多產品像咖啡、餅乾、鳳梨酥也有馬告口味唷～\n在過去，人們會將果實泡水飲用來緩解頭痛呢！")
        return msg
    elif ('馬告' in T and '知識' in T) or '關於馬告' in T:
        msg = TextSendMessage(text="馬告一名來自於泰雅族語Makauy，意指山胡椒且有充滿生機、生生不息的意思～\n馬告從上到下幾乎沒有無用之處，整株植物都可以被有效的利用！")
        return msg
    elif T == "幹":
        msg = TextSendMessage(text="幹三小？")
        return msg
    else:
        msg = TextSendMessage(text="抱歉～瑪糕還沒完善，不知道你在說甚麼。")
        return msg

#店家
def msglist_Store():
    message = TemplateSendMessage(
        alt_text='店家',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/AmUSVUp.png',
                    title='烏來泰雅農產合作社',
                    text='請按連結',
                    actions=[
                        URITemplateAction(
                            label='合作社',
                            uri='https://qulaw123.myorganic.org.tw/'
                        )
                    ]
                )
            ]
        )
    )
    return message

#選單_快速提問
def msglist_Template():
    message = TemplateSendMessage(
        alt_text='快問選單',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='快速提問─關於馬告',
                    text='請按按鈕',
                    actions=[
                        MessageTemplateAction(
                            label='關於馬告',
                            text='關於馬告'
                        )
                    ]
                ),
                CarouselColumn(
                    title='快速提問─馬告功效',
                    text='請按按鈕',
                    actions=[
                        MessageTemplateAction(
                            label='馬告功效',
                            text='馬告功效'
                        )
                    ]
                ),
                CarouselColumn(
                    title='快速提問─店家資訊',
                    text='請按按鈕',
                    actions=[
                        MessageTemplateAction(
                            label='店家資訊',
                            text='店家資訊'
                        )
                    ]
                ),
                CarouselColumn(
                    title='快速提問─產品示意圖',
                    text='請按按鈕',
                    actions=[
                        MessageTemplateAction(
                            label='產品示意圖',
                            text='產品示意圖'
                        )
                    ]
                )
            ]
        )
    )
    return message

#產品示意
def msglist_Product():
    message = TemplateSendMessage(
        alt_text='產品圖片',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/vneKgqG.jpg",
                    action=URITemplateAction(
                        label="馬告精油",
                        uri="https://img.ruten.com.tw/s2/3/57/06/21922572375814_841.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/qnGJF60.jpg",
                    action=URITemplateAction(
                        label="馬告鳳梨酥",
                        uri="https://b.blog.xuite.net/b/2/d/e/12584724/blog_32120/txt/292319961/19.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/qxvOQ9L.jpg",
                    action=URITemplateAction(
                        label="馬告玫瑰鹽",
                        uri="https://a.ecimg.tw/items/QFAI8TA9008ERHY/000001_1505376248.jpg"
                    )
                )
            ]
        )
    )
    return message


    


