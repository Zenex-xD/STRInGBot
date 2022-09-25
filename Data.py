from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}
🥀𝐖ᴇʟᴄᴏᴍᴇ 𝐓ᴏ {} 𝐁ot..! 💫 ᴀ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ.
[𝐗ᴅ](https://telegra.ph/file/cdc4b7391754d321318a2.jpg) ᴄʟɪᴄᴋ ᴏɴ ɢᴇɴʀᴀᴛᴇ sᴛʀɪɴɢ ғᴏʀ ɢᴇɴᴇʀᴀᴛ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ..!✨

♤ 𝐏ᴏᴡᴇʀᴇᴅ 🔥 𝐁ʏ: [𝐙ᴇᴜs•𝐗ᴅ](https://t.me/Arcane_bots)
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
        [InlineKeyboardButton("𝐒ᴇᴄʀᴀᴛᴇ 𝐗ᴅ", url="https://t.me/ArcaneXchatting")],
        [
            InlineKeyboardButton("𝐇ᴏᴡ ᴛᴏ ᴜsᴇ 📖❔", callback_data="help"),
            InlineKeyboardButton("♤ 𝐀ʙᴏᴜᴛ ♤", callback_data="about")
        ],
        [InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs", url="https://t.me/kiara_updates")],
    ]

    # Help Message
    HELP = """
🥀 **𝐴𝑣𝑎𝑖𝑙𝑎𝑏𝑙𝑒 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠** 🔥

/about - 𝑨𝒃𝒐𝒖𝒕 𝑻𝒉𝒆 𝑩𝒐𝒕
/help - 𝑻𝒉𝒊𝒔 𝑴𝒆𝒔𝒔𝒂𝒈𝒆
/start - 𝑺𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝑩𝒐𝒕
/generate - 𝑺𝒕𝒂𝒓𝒕 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒏𝒈 𝑺𝒆𝒔𝒔𝒊𝒐𝒏
/cancel - 𝑪𝒂𝒏𝒄𝒆𝒍 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔
/restart - 𝑪𝒂𝒏𝒄𝒆𝒍 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔
"""

    # About Message
    ABOUT = """
**About This Bot** 

𝐀 𝐓ᴇʟᴇɢʀᴀᴍ 𝐁ᴏᴛ ᴛᴏ 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐏ʏʀᴏɢʀᴀᴍ ᴀɴᴅ 𝐓ᴇʟᴇᴛʜᴏɴ 𝐒ᴛʀɪɴɢ 𝐒ᴇssɪᴏɴ...! 

𝐅ʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](docs.pyrogram.org)

𝐋ᴀɴɢᴜᴀɢᴇ : [Python](www.python.org)

𝐃ᴇᴠʟᴏᴘᴇʀ 𝐗ᴅ : [𝐙ᴇᴜs](http://t.me/ll_ZEUS_II)
    """
