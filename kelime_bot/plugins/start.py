from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Məni Qrupuna əlavə et ➕", url=f"http://t.me/SozTapbot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇦🇿 Sahib 👨‍💻", url="t.me/Thagiyevv")
    ],
    [
        InlineKeyboardButton("📢 Rəsmi Kanal ", url="https://t.me/RiyaddBlogg")
    ],
    [
        InlineKeyboardButton("💬 Söhbət Qrupu", url="https://t.me/KarabakhTeamm")  
    ]
])


START = """
**👋 Salam. Mən 𝕏𝔸𝕆𝕊 𝔾𝔸𝕄𝔼**

**⚡ Mən Qruplar üçün yaradılmış Rəsmi Oyun Botuyam**
**📌 Bu Bot İlə Qrupda Vaxtınızı Maraqlı Keçirə Bilərsiniz**

⚙ Əmrlər Üçün ➪ /help Əmrindən İsdifadə Edin 
✅ Əmrlər Asan Və Sadədir
"""

HELP = """
**⚙ Əmrlər Menyusu**

➪ /oyna - Yeni Oyuna Başla
➪  /kec - Sözü Dəyiş
➪ /dayan - Oyunu Dayandır
➪  /top - Bütün Qruplar Üzrə Oyunçuların Xalları
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://images.app.goo.gl/T13zSBpbjyvgT5nZ9",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://images.app.goo.gl/T13zSBpbjyvgT5nZ9",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyna")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Qrupunuzda Oyun Hal-Hazırda Oyun Davam Edir!\nℹ Oyunu Dayandırıb Yenidən Başlamaq Üçün /dayan Yazın Və Ya Oyuna Davam Etmək Üçün /kec Yazın")
    else:
        await m.reply(f"**{m.from_user.mention} **Tərəfindən\nSöz Oyunu Başladı !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund: {oyun[m.chat.id]['round']}/100
🌠 Tapılacaq Söz: <code>{kelime_list}</code>
📌 İpucu: {oyun[m.chat.id]["kelime"][0]}
🔗 Uzunluq: {int(len(kelime_list)/2)}
⏳ Qarışıq Yazılmış Bu Hərflərdən Əsas Sözü Tapmağa Çalış!
        """
        await c.send_message(m.chat.id, text)
        
