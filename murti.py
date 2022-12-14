import os, youtube_dl, requests, time
from config import Config
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import yt_dlp
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)


#config#

bot = Client(
    'moonBot',
    bot_token = "5644947301:AAHHRRTc6JeuvcizG4p24qxlkziwD01SYbw",
    api_id = "11385233",
    api_hash = "16d51f2c856dec1c9abf7f4b31fb9d6e",
)

#start mesajı

@bot.on_message(filters.command(['start']))
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAxUAAWNRxatAVFmPJbhvpJHlbYzmfLqlAAJaFQACujXpS7qkodxHjtB3KgQ")
    await message.reply_text(
    f"""🥂 **Merhaba** {message.from_user.mention}\n\n**🎵 Ben Basit Bir Müzik İndirme Botuyum**\n\n**Yardıma İhtiyacın Varsa** /yardim **Komutunu Kullan**""",
        reply_markup=InlineKeyboardMarkup(
            [[
                    InlineKeyboardButton('➕ Beni Gruba Ekle ➕', url=f'http://t.me/muzik_indiren_bot?startgroup=new'),
                  ],[
                    InlineKeyboardButton('🏹 Grubumuz', url=f'https://t.me/GalaSohbetTR'),
                    InlineKeyboardButton('🌹 Kanalımız', url=f'https://t.me/belkigununbirinde')
                  ],[
                    InlineKeyboardButton('👤 Sahip', url=f't.me/uslanmazmurti')
                ]
            ]
        )
    )
    
#yardim

@bot.on_message(filters.command(['yardim']))
def help(client, message):
    helptext = f'• **Müzik İndirmek İçin /ara Komutunu Kullan.**\n\n**Örneğin** :\n•> /ara `Tut Elimden`'
    message.reply_text(
        text=helptext, 
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [[
                    InlineKeyboardButton('🎵 Playlist', url=f'http://t.me/playlistmp3murti'),
                  ],[
                    InlineKeyboardButton('☠ Botlarım', url=f'https://t.me/murtibots'),
                    InlineKeyboardButton('🍃 Ana Bot', url=f'https://t.me/murtix_bot')
                  ],[
                    InlineKeyboardButton('🎮 Oyun & Film Botumuz', url=f'https://t.me/inekgame_bot')
                ]
            ]
        )
    )
#alive#

@bot.on_message(filters.command("alive") & filters.user(Config.BOT_OWNER))
async def live(client: Client, message: Message):
    livemsg = await message.reply_text('`Selam` **@uslanmazmurti** `Emrindeyim 🌹`')
    
#muxik indirme#

@bot.on_message(filters.command("ara") & ~filters.edited)
def bul(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("🔎")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("<b>⛔ **Üzgünüm Şarkıyı Bulamadım.**</b>")
        print(str(e))
        return
    m.edit("<b>•> **İndirme Başlatıldı...**</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"[➕ BOTU GRUBA EKLE ➕](https://t.me/muzik_indiren_bot?startgroup=a)\n\n╠══════════════════╣\n➥[🎵 Mp3 İndiren Bot](https://t.me/muzik_indiren_bot)\n➥[🎶 Çalma Listesi](https://t.me/PlayListMp3Murti)\n➥[🤖 Diğer Botlar](https://t.me/MurtiBots)\n╠══════════════════╣"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("•> **Yüklüyorum**...")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@uslanmazmurti")
        m.delete()
        bot.send_audio(chat_id=-1001820185928, audio=audio_file, caption=rep, performer="@uslanmazmurti", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit("<b>⛔ **Hata Bekle Ve Tekrar Dene** .</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

bot.run()
