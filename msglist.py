from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#關鍵字清單
def replay_msglist(T):
    if '你好' in T :
        msg = TextSendMessage(text="你好～這裡是瑪糕～")
        return msg
    elif '馬告' in T and '功效' in T:
        msg = TextSendMessage(text="馬告具有安眠、鎮痛與抗憂的功效喲～")
        return msg
    elif T == "幹":
        msg = TextSendMessage(text="幹三小？")
        return msg
        
#選單_快速提問
def msglist_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='',
                            data=''
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='',
                            uri=''
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
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


    


