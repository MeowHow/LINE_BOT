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
        
#店家
def msglist_Store():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='店家',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                link_uri="https://qulaw123.myorganic.org.tw/",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
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


    


