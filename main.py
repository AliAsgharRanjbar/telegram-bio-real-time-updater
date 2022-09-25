from time import time
from time import sleep
from telethon.sync import TelegramClient
from datetime import datetime
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
import random

api_id = 2776086
api_hash = "a873cc6bf92417d1fd96c865522c96a5"
session_name = '.session'

font1 = "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
font2 = "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"
font3 = "⓪①②③④⑤⑥⑦⑧⑨"
font4 = "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
font5 = "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
font6 = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"

fonts = [font1, font2, font3, font4, font5, font6]


def bio_clock_font(clock):
    x = "0123456789"
    y = random.choice(fonts)
    my_table = clock.maketrans(x, y)
    return clock.translate(my_table)


def name_clock_font(clock):
    x = "0123456789"
    y = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    my_table = clock.maketrans(x, y)
    return clock.translate(my_table)


with TelegramClient(session_name, api_id, api_hash) as client:

    while True:
        if round(time()) % 60 == 0:
            sleep(1)
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            hour = now.strftime("%H")
            hour = int(hour)

            text = current_time
            bio_text = f"『{bio_clock_font(text)}』"
            lastname_text = name_clock_font(text)

            if 00 <= hour <= 11:
                profile_bio = f'ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌅 | {bio_text}'

                client(UpdateProfileRequest(about=profile_bio))

            elif 12 <= hour <= 17:
                profile_bio = f'ʙᴜᴇɴᴀꜱ ᴛᴀʀᴅᴇꜱ ☀ | {bio_text}'

                client(UpdateProfileRequest(about=profile_bio))

            elif 18 <= hour <= 21:
                profile_bio = f'ДОБРЫЙ ВЕЧЕР ⭐ | {bio_text}'

                client(UpdateProfileRequest(about=profile_bio))

            else:
                profile_bio = f'안녕히 주무세요 🌙 | {bio_text}'

                client(UpdateProfileRequest(about=profile_bio))

            client(UpdateProfileRequest(first_name="ᴀʟɪ"))
            client(UpdateProfileRequest(last_name=f"『{lastname_text}』"))

            print(profile_bio, lastname_text)

