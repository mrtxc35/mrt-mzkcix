

########
                    # 
                   # 
    # Kodu değiştirmeyin. Bunu kullanmak istiyorsanız Kendinize alın ancak burayı değiştirmeyin              #
       #      @erdem4455vip tarafından kodlandı	    #
                   #
 ########                 
                                        



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
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

#start mesajı

@bot.on_message(filters.command(['start']))
async def start_(client: Client, message: Message):
    await message.reply_text("GELIŞTIRICI VE GÜNCELLEYICI : @erdem4455vip")
    await message.reply_text(
    f"""🥂 **Merhaba** {message.from_user.mention}\n\nʙᴇɴ sᴜ̈ᴘᴇʀ ʜɪᴢɪᴍ ɪʟᴇ ᴍᴜ̈ᴢɪᴋ/ᴠɪᴅᴇᴏ ɪɴᴅɪʀᴍᴇɴ ɪᴄ̧ɪɴ ʏᴀʀᴀᴛɪʟᴅɪᴍ.\n\n𝙳𝚊𝚑𝚊 𝚏𝚊𝚣𝚕𝚊 𝚋𝚒𝚕𝚐𝚒 𝚟𝚎 𝚔𝚘𝚖𝚞𝚝 𝚋𝚒𝚕𝚐𝚒𝚜𝚒 𝚒𝚌̧𝚒𝚗 : /help\n**Bot hakkında bilgi almak için : /botbilgi**""",
        reply_markup=InlineKeyboardMarkup(
            [[
                    InlineKeyboardButton('➕ 𝐛𝐞𝐧𝐢 𝐠𝐫𝐮𝐛𝐮𝐧𝐚 𝐞𝐤𝐥𝐞➕', url=f'http://t.me/Music_installer31_bot?startgroup=bew'),
                  ],[
                    InlineKeyboardButton('🏹 𝕤𝕠𝕙𝕓𝕖𝕥/𝕕𝕖𝕤𝕥𝕖𝕜', url=f'https://t.me/pubglitefucker'),
                    InlineKeyboardButton('🌹 ɢᴜ̈ɴᴄᴇʟʟᴇᴍᴇʟᴇʀ', url=f'https://t.me/techosbots')
                  ],[
                    InlineKeyboardButton('👤 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥', url=f't.me/erdem4455vip')
                ]
            ]
        )
    )
    
#help

@bot.on_message(filters.command(['help']))
def help(client, message):
    helptext = f'• **Müzik İndirmek İçin /ara Komutunu Kullan.**\n **Video indirmek için /arvid komutunu kullan**\n\n :\n•> /ara `Tut Elimden`\n /arvid `tut sikimden`'
    message.reply_text(
        text=helptext, 
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [[
                    InlineKeyboardButton('🎵 Playlist', url=f'http://t.me/music_installer31_playlist'),
                  ],[
                    InlineKeyboardButton('✨ Destek', url=f'https://t.me/pubglitefucker'),
                    InlineKeyboardButton('🍃 Tagger Bot', url=f'https://t.me/stor_tagger_bot')
                  ],[
                    InlineKeyboardButton('🎮 Oyun  Botumuz', url=f"https://t.me/hesap_game_bot')
                ]
            ]
        )
    )
#alive#

@bot.on_message(filters.command("alive") & filters.user(Config.BOT_OWNER))
async def live(client: Client, message: Message):
    livemsg = await message.reply_text('`Selam @erdem4455vip Emrindeyim 🌹`')
    
#muzik indirme#
@bot.on_message(filters.command('botbilgi'))
def botbilgi(_, message):
bot.send_message(message.chat.id,"𝐤𝐨𝐝𝐥𝐚𝐧𝐝𝛊𝐠̆𝛊𝐦 𝐝𝐢𝐥 : 𝐩𝐲𝐭𝐡𝐨𝐧\n 𝗿𝗲𝗽𝗼 : __🚫 Benden alıp parayla sattıkları için kapandı__")
@bot.on_message(filters.command("ara") & ~filters.edited)
def bul(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>• **Şarkıyı Arıyorum** ...</b>")
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
        m.edit("⛔__Burayı boş bıraktınız ya da geçersiz bir ad verdiniz.!__📴")
        
        print(str(e))
        return
    m.edit("<b>•> **İndirme Başlatıldı...**</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"🎵 [Music Bot](https://t.me/Music_installer31_bot) Sizin İçin Araştırdı!"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("•> **Yüklüyorum**...")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@erdem4455vip")
        m.delete()
        # Playlist id yi {} içind alarakta dene
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=rep, performer="@erdem4455vip", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit("<b>⛔ **Hata Bekle Ve Tekrar Dene** .</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
        # video ya geçiş
@bot.on_message(filters.command('arvid') & ~filters.edited)        
message.reply_text("ᴠɪᴅᴇᴏ ʏᴜ̈ᴋʟᴇᴍᴇ ᴏ̈ᴢᴇʟʟɪɢ̆ɪ ʙᴇᴛᴀᴅɪʀ. ᑕ̧ᗩᒪIᔕ̧ᗰᗩYᗩᗷIᒪIᖇ...")
        def bulvid(_, message):
    query = " ".join(message.command[1:])
    e = message.reply("<b>• **Videoyu Arıyorum** ...</b>")
    ydl_ops = {"format": "bestvideo[ext=mp4]"}
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
        e.edit("<b>⛔ **Üzgünüm Videoyu Bulamadım.**</b>")
        print(str(e))
        return
    e.edit("<b>•> **İndirme Başlatıldı...**</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            video_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"💽 [𝐯𝐢𝐝𝐞𝐨/𝐦𝐮𝐬𝐢𝐜 Bot](https://t.me/Music_installer31_bot) Sizin İçin Araştırdı!"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        e.edit("•> **Yüklüyorum㋛︎シ︎**...")
        
        message.reply_video(video_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@erdem4455vip")
        e.delete()
       # Playlist id yi {} içind alarakta dene
        bot.send_video(chat_id=Config.PLAYLIST_ID, video=video_file, caption=rep, performer="@erdem4455vip", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        e.edit("<b>⛔ **Hata Bekle Ve Tekrar Dene** .</b>")
        print(e)
        
    try:
        os.remove(video_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

bot.run()

# Coder = https://t.me/erdem4455vip