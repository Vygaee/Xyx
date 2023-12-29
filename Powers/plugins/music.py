from random import choice

from pyrogram import enums, filters
from pyrogram.errors import MediaCaptionTooLong
from pyrogram.types import CallbackQuery, Message

from Powers import LOGGER
from Powers.bot_class import Gojo
from Powers.utils.custom_filters import command
from Powers.utils.extras import StartPic
from Powers.utils.kbhelpers import ikb


@Gojo.on_callback_query(filters.regex("printah_"))
async def musik_owner_help(client, cb):
    query = cb.data
    userid = cb.message.chat.id
    data = query.split("_")[1]
    if data == "musik":
        text = """**Printah Admin:**
        
 **c** adalah singkatan dari pemutaran saluran.

/pause atau /cpause - Menjeda musik yang sedang diputar.
/resume atau /cresume- Melanjutkan musik yang dijeda.
/mute atau /cmute- Mematikan musik yang diputar.
/unmute atau /cunmute- Mengaktifkan musik yang dimatikan.
/skip atau /cskip- Lewati musik yang sedang diputar.
/stop atau /cstop- Menghentikan pemutaran musik.
/shuffle atau /cshuffle- Secara acak mengacak daftar putar yang antri.

**Lewati Spesifik:*
/skip atau /cskip
    - Melompati musik ke nomor antrian yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅**Pemutaran Putaran:*
/loop atau /cloop aktifkan/nonaktifkan atau Angka antara 1-10
    - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default untuk 10 kali.

✅**Pengguna Auth:*
Pengguna Auth dapat menggunakan perintah admin tanpa hak admin di obrolan Anda.

/auth Nama Pengguna - Tambahkan pengguna ke DAFTAR AUTH grup.
/unauth Nama Pengguna - Menghapus pengguna dari DAFTAR AUTH grup.
/authusers - Periksa DAFTAR AUTH grup. """
        
    elif data == "musik_":
        text = """**Printah Play:**

**cplay** atau **cstream **singkatan dari channel play.
**vplay** adalah singkatan dari pemutaran video.

/play atau /vplay atau /cplay - Bot akan mulai memainkan kueri yang Anda berikan pada obrolan suara.

/stream atau /cstream - Streaming tautan langsung di obrolan suara.

/channelplay Nama pengguna atau id obrolan atau Nonaktifkan - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.


**Daftar Putar Server Bot:**
/playlist - Periksa Daftar Putar Tersimpan Anda Di Server.
/deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda
/play - Mulai mainkan Daftar Putar Tersimpan Anda dari Server.
 """
    else:
        text = """**Bantuan Printah Musik:**
Pilih Menu Dibawah Ini Untuk Melihat Bantuan Printah Musik
"""
    await cb.message.edit(
        text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Printah Admin", callback_data="py_"),
                    InlineKeyboardButton(
                        "Printah Play", callback_data="mus_"),
                ],
                [
                    InlineKeyboardButton(
                        "Printah Bot", callback_data="musik_"),
                    InlineKeyboardButton(
                        "Printah Extra", callback_data="exstra_"),
                ],
                [
                    InlineKeyboardButton("⚙️ Back Manage", callback_data="help_back"),                               
               ],
            ]
        ),
        parse_mode=ParseMode.MARKDOWN,
  )


async def gen_help_kb(m):
    return ikb(
        [
            [
                ("Admin", "Play"),
                ("Bot", "Ekstra"),
            ],
            [("Random Music", "Random Manage")],
        ],
        True,
        "commands"
    )


@Gojo.on_message(
    command(["mhelp", "Music"]) & filters.private,
)
async def markdownhelp(_, m: Message):
    await m.reply_photo(
        photo=str(choice(StartPic)),
        caption=f"{__HELP__}",
        quote=True,
        reply_markup=(await gen_formatting_kb(m)),
    )
    LOGGER.info(f"{m.from_user.id} used cmd '{m.command}' in {m.chat.id}")
    return


@Gojo.on_callback_query(filters.regex("^Music."))
async def get_Music_info(c: Gojo, q: CallbackQuery):
    cmd = q.data.split(".")[1]
    kb = ikb([[("Back", "back.Music")]])

    if cmd == "md_music":
        
        txt = """<b>Markdown Formatting</b>
You can format your message using <b>bold</b>, <i>italic</i>, <u>underline</u>, <strike>strike</strike> and much more. Go ahead and experiment!

**Note**: It supports telegram user based formatting as well as html and markdown formattings.
<b>Supported markdown</b>:
- <code>`code words`</code>: Backticks are used for monospace fonts. Shows as: <code>code words</code>.
- <code>__italic__</code>: Underscores are used for italic fonts. Shows as: <i>italic words</i>.
- <code>**bold**</code>: Asterisks are used for bold fonts. Shows as: <b>bold words</b>.
- <code>```pre```</code>: To make the formatter ignore other formatting characters inside the text formatted with '```', like: <code>**bold** | *bold*</code>.
- <code>--underline--</code>: To make text <u>underline</u>.
- <code>~~strike~~</code>: Tildes are used for strikethrough. Shows as: <strike>strike</strike>.
- <code>||spoiler||</code>: Double vertical bars are used for spoilers. Shows as: <spoiler>Spoiler</spoiler>.
- <code>[hyperlink](example.com)</code>: This is the formatting used for hyperlinks. Shows as: <a href="https://example.com/">hyperlink</a>.
- <code>[My Button](buttonurl://example.com)</code>: This is the formatting used for creating buttons. This example will create a button named "My button" which opens <code>example.com</code> when clicked.
If you would like to send buttons on the same row, use the <code>:same</code> formatting.
<b>Example:</b>
<code>[button 1](buttonurl:example.com)</code>
<code>[button 2](buttonurl://example.com:same)</code>
<code>[button 3](buttonurl://example.com)</code>
This will show button 1 and 2 on the same line, while 3 will be underneath."""
        try:
            await q.edit_message_caption(
                caption=txt,
                reply_markup=kb,
                parse_mode=enums.ParseMode.HTML,
            )
        except MediaCaptionTooLong:
            await c.send_message(
                chat_id=q.message.chat.id,
                text=txt,
                parse_mode=enums.ParseMode.HTML,)
    elif cmd == "Play":
        await q.edit_message_caption(
            caption="""<b>Play</b>

You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the welcome message, or mention them in a filter!
You can use these to mention a user in notes too!

<b>Supported fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code>{fullname}</code>: The user's full name.
- <code>{username}</code>: The user's username. If they don't have one, mentions the user instead.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{chatname}</code>: The chat's name.""",
            reply_markup=kb,
            parse_mode=enums.ParseMode.HTML,
        )
    elif cmd == "Bot":
        await q.edit_message_caption(
            caption="""<b>Random Content</b>

Another thing that can be fun, is to randomise the contents of a message. Make things a little more personal by changing welcome messages, or changing notes!

How to use random contents:
- %%%: This separator can be used to add "random" replies to the bot.
For example:
<code>hello
%%%
how are you</code>
This will randomly choose between sending the first message, "hello", or the second message, "how are you".
Use this to make Gojo feel a bit more customised! (only works in filters/notes)

Example welcome message::
- Every time a new user joins, they'll be presented with one of the three messages shown here.
-> /filter "hey"
hello there <code>{first}</code>!
%%%
Ooooh, <code>{first}</code> how are you?
%%%
Sup? <code>{first}</code>""",
            reply_markup=kb,
            parse_mode=enums.ParseMode.HTML,
        )

    await q.answer()
    return


@Gojo.on_callback_query(filters.regex("^back."))
async def send_mod_help(_, q: CallbackQuery):
    await q.edit_message_caption(
        caption="""Music

Gojo supports a large number of formatting options to make your messages more expressive. Take a look by clicking the buttons below!""",
        reply_markup=(await gen_formatting_kb(q.message)),
    )
    await q.answer()
    return


__PLUGIN__ = "Music"

__alt_name__ = ["Admin", "Play", "Bot", "Extra"]
__buttons__ = [
    [
        ("Admin", "Play"),
        ("Bot", "Extra"),
    ],
    [("Random Music", "Random Manage")],
]

__HELP__ = """
**Music**

Gojo supports a large number of formatting options to make your messages more expressive. Take a look by clicking the buttons below!"""
