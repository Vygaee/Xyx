
from random import choice

from pyrogram import enums, filters
from pyrogram.errors import MediaCaptionTooLong
from pyrogram.types import CallbackQuery, Message

from Powers import LOGGER
from Powers.bot_class import Gojo
from Powers.utils.custom_filters import command
from Powers.utils.extras import StartPic
from Powers.utils.kbhelpers import ikb

   
@Gojo.on_callback_query(filters.regex("^formatting."))
async def get_formatting_info(c: Gojo, q: CallbackQuery):
    cmd = q.data.split(".")[1]
    kb = ikb([[("Back", "back.formatting")]])

    if cmd == "md_formatting":
        
        txt = """<b>Admin</b>
 c adalah singkatan dari pemutaran saluran.

/pause atau /cpause - Menjeda musik yang sedang diputar.
/resume atau /cresume- Melanjutkan musik yang dijeda.
/mute atau /cmute- Mematikan musik yang diputar.
/unmute atau /cunmute- Mengaktifkan musik yang dimatikan.
/skip atau /cskip- Lewati musik yang sedang diputar.
/stop atau /cstop- Menghentikan pemutaran musik.
/shuffle atau /cshuffle- Secara acak mengacak daftar putar yang antri.

**Lewati Spesifik:*
/skip atau /cskip
Melompati musik ke nomor antrian yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅**Pemutaran Putaran:*
/loop atau /cloop aktifkan/nonaktifkan atau Angka antara 1-10
Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default untuk 10 kali.

✅**Pengguna Auth:*
Pengguna Auth dapat menggunakan perintah admin tanpa hak admin di obrolan Anda.

/auth Nama Pengguna - Tambahkan pengguna ke DAFTAR AUTH grup.
/unauth Nama Pengguna - Menghapus pengguna dari DAFTAR AUTH grup.
/authusers - Periksa DAFTAR AUTH grup."""
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
    elif cmd == "fillings":
        await q.edit_message_caption(
            caption="""<b>Play</b>

**cplay** atau **cstream **singkatan dari channel play.
**vplay** adalah singkatan dari pemutaran video.

/play atau /vplay atau /cplay - Bot akan mulai memainkan kueri yang Anda berikan pada obrolan suara.

/stream atau /cstream - Streaming tautan langsung di obrolan suara.

/channelplay Nama pengguna atau id obrolan atau Nonaktifkan - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.

**Daftar Putar Server Bot:**
/playlist - Periksa Daftar Putar Tersimpan Anda Di Server.
/deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda
/play - Mulai mainkan Daftar Putar Tersimpan Anda dari Server.""",
            reply_markup=kb,
            parse_mode=enums.ParseMode.HTML,
        )
    elif cmd == "random_content":
        await q.edit_message_caption(
            caption="""<b>Bot/Extra</b>

<b>✅ Perintah Bot:</b>
/stats - Dapatkan Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat, dll.

/sudolist - Periksa Pengguna Sudo dari Bot Musik Musikku

/lyrics Music Name - Mencari Lirik untuk Musik tertentu di web.

/song Nama Trek atau Tautan YT - Unduh trek apa pun dari youtube dalam format mp3 atau mp4.

c adalah singkatan dari pemutaran saluran.
/queue atau /cqueue- Periksa Daftar Antrian Musik

<b>Printah Extra</b>
✅ Perintah Ekstra:
/start - Mulai Bot Musik.
/help - Dapatkan Menu Helper Perintah dengan penjelasan rinci tentang perintah.
/ping - Ping Bot dan periksa Ram, Cpu dll statistik Bot.

Setelan Grup
Anda dapat mengatur Kualitas Audio yang ingin Anda streaming di obrolan suara.
✅ Pengguna Auth : Anda dapat mengubah mode perintah admin dari sini ke semua orang atau hanya admin.
✅ Mode Bersih : Saat diaktifkan, hapus pesan bot setelah 5 menit dari grup Anda untuk memastikan obrolan Anda tetap bersih dan baik.
✅ Command Clean : Saat diaktifkan, Bot akan segera menghapus perintah yang dijalankannya /play, /pause, /shuffle, /stop dll.

Pengaturan Putar
/playmode - Dapatkan panel pengaturan pemutaran lengkap dengan tombol di mana Anda dapat mengatur pengaturan pemutaran grup Anda.
Direct or Inline - Mengubah mode pencarian saat Anda memberikan mode /play.
Tipe Putar Semua Orang atau Admin - Jika admin, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara.""",
            reply_markup=kb,
            parse_mode=enums.ParseMode.HTML,
        )

    await q.answer()
    return


@Gojo.on_callback_query(filters.regex("^back."))
async def send_mod_help(_, q: CallbackQuery):
    await q.edit_message_caption(
        caption="""Formatting

Gojo supports a large number of formatting options to make your messages more expressive. Take a look by clicking the buttons below!""",
        reply_markup=(await gen_formatting_kb(q.message)),
    )
    await q.answer()
    return


__PLUGIN__ = "music"

__alt_name__ = ["formatting", "markdownhelp", "markdown"]
__buttons__ = [
    [
        ("Markdown Formatting", "formatting.md_formatting"),
        ("Fillings", "formatting.fillings"),
    ],
    [("Random Content", "formatting.random_content")],
]

__HELP__ = """
**Bantuan Music**

Gojo supports a large number of formatting options to make your messages more expressive. Take a look by clicking the buttons below!"""
