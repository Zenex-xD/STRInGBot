from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}
🥀𝐖ᴇʟᴄᴏᴍᴇ 𝐓ᴏ {} 𝐁ot..! ᴀ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ.
[𝐗ᴅ](https://telegra.ph/file/cdc4b7391754d321318a2.jpg) ᴄʟɪᴄᴋ ᴏɴ ɢᴇɴʀᴀᴛᴇ sᴛʀɪɴɢ ғᴏʀ ɢᴇɴᴇʀᴀᴛ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ..!✨

♤ 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ: [𝐗ᴅ](https://t.me/About_Zenex)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("𝐆ᴇɴʀᴀᴛᴇ 𝐒ᴇssɪᴏɴ", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("𝐆ᴇɴʀᴀᴛᴇ 𝑺ᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("𝐆ᴇɴʀᴀᴛᴇ 𝐒ᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("𝐒ᴇᴄʀᴀᴛᴇ 𝐗ᴅ", url="https://t.me/ABOUT_ZENEX")],
        [
            InlineKeyboardButton("𝐇ᴏᴡ ᴛᴏ ᴜsᴇ 📖❔", callback_data="help"),
            InlineKeyboardButton("♤ 𝐀ʙᴏᴜᴛ ♤", callback_data="about")
        ],
        [InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs", url="https://t.me/About_Zenex")],
    ]

    # Help Message
    HELP = """
🥀 **𝐴𝑣𝑎𝑖𝑙𝑎𝑏𝑙𝑒 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠** 🔥

/about - ɪɴғᴏ ᴏғ ʙᴏᴛ
/help - ʜᴏᴡ ᴛᴏ ᴜsᴇ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/generate - ɢᴇɴʀᴀᴛᴇ sᴇs
/cancel - sᴛᴏᴘ ʙᴏᴛ 
/restart - ʀᴇɢᴇɴʀᴀᴛᴇ ʏᴏᴜʀ sᴛʀɪɴɢ ᴀɢᴀɪɴ
"""

    # About Message
    ABOUT = """
**About This Bot** 

𝐀 𝐓ᴇʟᴇɢʀᴀᴍ 𝐁ᴏᴛ ᴛᴏ 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐏ʏʀᴏɢʀᴀᴍ ᴀɴᴅ 𝐓ᴇʟᴇᴛʜᴏɴ 𝐒ᴛʀɪɴɢ 𝐒ᴇssɪᴏɴ...! 

𝐅ʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](docs.pyrogram.org)

𝐋ᴀɴɢᴜᴀɢᴇ : [Python](www.python.org)

𝐃ᴇᴠʟᴏᴘᴇʀ 𝐗ᴅ : [𝐙ᴇᴜs](http://t.me/ZENEX_XD)
    """
