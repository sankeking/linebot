# 運行以下程式需安裝模組: line-bot-sdk, flask, pyquery
# 安裝方式，輸入指令: pip install 模組名稱

# 引入flask模組
from flask import Flask, request, abort
# 引入linebot相關模組
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

# 如需增加其他處理器請參閱以下網址的 Message objects 章節
# https://github.com/line/line-bot-sdk-python
from linebot.models import (
    MessageEvent,
    TextMessage,
    StickerMessage,
    TextSendMessage,
    StickerSendMessage,
    LocationSendMessage,
    ImageSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction,
    MessageAction,
    URIAction,
    CarouselTemplate,
    CarouselColumn
)
from modules.reply import faq, menu
app = Flask(__name__)

# 更新以下資料為自己的TOKEN與SECRET
CHANNEL_ACCESS_TOKEN = '70tf0Ixsn8fpdym1Y5EwLREc6E3ZA2DlgkCaMaHINdnaWRErBhm7ZHs92VhV5oVH0YMMg7W+j7hlDhnErXZPs6hP1mhJoIDcIcE9RbfpzXP1Ntr36ROZ7L0YJnQJHAidYeO3nN/3W2U+NHxUhqvqxAdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '9bbcd03ac50228a9dd194eee00330d2c'

# ********* 以下為 X-LINE-SIGNATURE 驗證程序 *********
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    print("[已接收訊息]")
    print(body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
# ********* 以上為 X-LINE-SIGNATURE 驗證程序 *********


# 文字訊息傳入時的處理器
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 當有文字訊息傳入時
    # event.message.text : 使用者輸入的訊息內容
    print('*'*30)
    print('[使用者傳入文字訊息]')
    print(str(event))
    # 取得使用者說的文字
    user_msg = event.message.text
    # 準備要回傳的文字訊息
    reply = menu

    if user_msg in faq:
        reply = faq[user_msg]

    # 筆記
    # reply = TextSendMessage(text=f'Hi，你剛才說的是「{user_msg}」對吧！')
    # 如果用戶問地址回應地址
    # if user_msg == "地址":
    #     reply = TextSendMessage(text="台北市文山區XX路")
    # elif user_msg == "電話":
    #     reply = TextSendMessage(text="02-2345-6789")
    # elif user_msg == "營業時間":
    #     reply = TextSendMessage(text="09:00-18:00")

    # 回傳訊息
    # 若需要回覆多筆訊息可使用
    # line_bot_api.reply_message(token, [Object, Object, ...])
    line_bot_api.reply_message(
        event.reply_token,
        reply)


# 貼圖訊息傳入時的處理器 
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    # 當有貼圖訊息傳入時
    print('*'*30)
    print('[使用者傳入貼圖訊息]')
    print(str(event))

    # 準備要回傳的貼圖訊息
    # HINT: 機器人可用的貼圖 https://devdocs.line.me/files/sticker_list.pdf
    reply = StickerSendMessage(package_id='2', sticker_id='144')

    # 回傳訊息
    line_bot_api.reply_message(
        event.reply_token,
        reply)


import os
if __name__ == "__main__":
    print('[伺服器開始運行]')
    # 取得遠端環境使用的連接端口，若是在本機端測試則預設開啟於port=5500
    port = int(os.environ.get('PORT', 5500))
    # 使app開始在此連接端口上運行
    print(f'[Flask運行於連接端口:{port}]')
    # 本機測試使用127.0.0.1, debug=True
    # Heroku部署使用 0.0.0.0
    app.run(host='0.0.0.0', port=port, debug=True)
