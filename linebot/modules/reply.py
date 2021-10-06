from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn, QuickReply, QuickReplyButton
)

# 官方文件
# https://github.com/line/line-bot-sdk-python

# 常見問答表
faq = {
    '貼圖': StickerSendMessage(
        package_id='2',
        sticker_id='149'
    ),
    '門市照片': ImageSendMessage(
        original_content_url='https://mapio.net/images-p/18425966.jpg',
        preview_image_url='https://mapio.net/images-p/18425966.jpg'
    ),
    '交通': TextSendMessage(text='請問您想使用何種方式前往？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="搭乘火車", text="火車")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="搭乘公車", text="公車")
                              )
                          ])
                          ),
    '火車': TextSendMessage(
        text="搭乘火車至宜蘭站步行5分鐘即可抵達。"
    ),
    '公車': TextSendMessage(
        text="搭乘公車至宜蘭火車站步行5分鐘即可抵達。"
    ),
    '營業地址': LocationSendMessage(
        title="McDonald's",
        address='Yilan',
        latitude=24.75681074167499,
        longitude=121.75816124414321
    ),
    '營業時間': TextSendMessage(
        text="24小時營業。"
    ),
    '簡介': TextSendMessage(
        text="麥當勞提供美味的漢堡、薯條、麥脆鷄（炸鷄）、冰炫風、沙拉、蘋果派等豐富的餐點、飲料與點心，讓您每次都能體驗麥當勞的方便與美食。"
    )
}

# 主選單
menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                # 卡片一圖片網址
                thumbnail_image_url='https://yt3.ggpht.com/ytc/AAUvwnhmXKGNujXUwxbA_qOUCwAwIdNxlmZb1WCOUN89Dw=s900-c-k-c0x00ffffff-no-rj',
                title='餐廳介紹',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='觀看簡介',
                        text='簡介'
                    ),
                    MessageAction(
                        label='營業時間',
                        text='營業時間'
                    ),
                    MessageAction(
                        label='營業地址',
                        text='營業地址'
                    )
                ]
            ),
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url='https://resource01-proxy.ulifestyle.com.hk/res/v3/image/content/2275000/2276895/1-HyVcB7vvVIx6N8Euj1t7Pg_600.jpeg',
                title='其他資訊',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='交通資訊',
                        text='交通'
                    ),
                    MessageAction(
                        label='門市照片',
                        text='門市照片'
                    ),
                    URIAction(
                        label='官方網站',
                        uri='https://www.mcdonalds.com/tw/zh-tw.html'
                    )
                ]
            )
        ]
    )
)
