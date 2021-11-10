# -*- coding: utf-8 -*-
"""
line Bot聊天機器人
第一章 Line Bot申請與串接
Line Bot機器人串接與測試
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

import random

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('QLdQ49iminM9vWWNHBX/lEXE5Y6Nufzu1YLPsQnRMXwy22aDO/XUeCzFOKsw5Y+REgpPVSZYdjTIdBkkb6YEoT63p4zfFehfRpwN7lbVD/Z6rCt3v/29KXxQkGfeER6NNfCcTamC5YSQiP2ZRehbngdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('e21b7c4fcde587a113145986d76bd68d')

line_bot_api.push_message('U41640217301124092e0eb4b6fd6bd49e', TextSendMessage(text='你可以開始了'))

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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('抽獎開始',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('準備開獎囉!'))
        
        line_bot_api.reply_message(event.reply_token,TextSendMessage(random,randint(1,10)))

    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
