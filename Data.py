from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}
ð¥ðá´Êá´á´á´á´ ðá´ {} ðot..! á´ á´ÊÊá´É¢Êá´á´ á´É´á´ á´á´Êá´á´Êá´É´ sá´ÊÉªÉ´É¢ É¢á´É´ Êá´á´.
[ðá´](https://telegra.ph/file/cdc4b7391754d321318a2.jpg) á´ÊÉªá´á´ á´É´ É¢á´É´Êá´á´á´ sá´ÊÉªÉ´É¢ Òá´Ê É¢á´É´á´Êá´á´ Êá´á´Ê sá´ÊÉªÉ´É¢ sá´ssÉªá´É´..!â¨

â¤ ðá´á´¡á´Êá´á´ ðÊ: [ðá´](https://t.me/About_Zenex)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("ðá´É´Êá´á´á´ ðá´ssÉªá´É´", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("ðá´É´Êá´á´á´ ðºá´ssÉªá´É´", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("ðá´É´Êá´á´á´ ðá´ssÉªá´É´", callback_data="generate")],
        [InlineKeyboardButton("ðá´á´Êá´á´á´ ðá´", url="https://t.me/ABOUT_ZENEX")],
        [
            InlineKeyboardButton("ðá´á´¡ á´á´ á´sá´ ðâ", callback_data="help"),
            InlineKeyboardButton("â¤ ðÊá´á´á´ â¤", callback_data="about")
        ],
        [InlineKeyboardButton("ðá´á´á´á´á´s", url="https://t.me/About_Zenex")],
    ]

    # Help Message
    HELP = """
ð¥ **ð´ð£ððððððð ð¶ððððððð ** ð¥

/about - ÉªÉ´Òá´ á´Ò Êá´á´
/help - Êá´á´¡ á´á´ á´sá´
/start - sá´á´Êá´ á´Êá´ Êá´á´
/generate - É¢á´É´Êá´á´á´ sá´s
/cancel - sá´á´á´ Êá´á´ 
/restart - Êá´É¢á´É´Êá´á´á´ Êá´á´Ê sá´ÊÉªÉ´É¢ á´É¢á´ÉªÉ´
"""

    # About Message
    ABOUT = """
**About This Bot** 

ð ðá´Êá´É¢Êá´á´ ðá´á´ á´á´ ðá´É´á´Êá´á´á´ ðÊÊá´É¢Êá´á´ á´É´á´ ðá´Êá´á´Êá´É´ ðá´ÊÉªÉ´É¢ ðá´ssÉªá´É´...! 

ðÊá´á´á´á´¡á´Êá´ : [Pyrogram](docs.pyrogram.org)

ðá´É´É¢á´á´É¢á´ : [Python](www.python.org)

ðá´á´ Êá´á´á´Ê ðá´ : [ðá´á´s](http://t.me/ZENEX_XD)
    """
