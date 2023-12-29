from random import choice

from pyrogram import enums, filters
from pyrogram.errors import MediaCaptionTooLong
from pyrogram.types import CallbackQuery, Message

from Powers import LOGGER
from Powers.bot_class import Gojo
from Powers.utils.custom_filters import command
from Powers.utils.extras import StartPic
from Powers.utils.kbhelpers import ikb


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
