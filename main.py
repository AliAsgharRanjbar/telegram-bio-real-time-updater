import asyncio
from pyrogram import Client
from time import time, sleep       # Importing required packages
from datetime import datetime
import random
import uvloop
from pytz import timezone


api_id = 123456789 # Your API_ID, You can get it from "https://my.telegram.org/"
api_hash = "abcdef123456" # Your API_hash, You can get it from "https://my.telegram.org/"

# Different fonts to be randomized everytime

font1 = "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
font2 = "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"
font3 = "⓪①②③④⑤⑥⑦⑧⑨"
font4 = "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
font5 = "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
font6 = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"

fonts = [font1, font2, font3, font4, font5, font6]

# Translating numbers to a random font

def bio_clock_font(clock):
    x = "0123456789"
    y = random.choice(fonts)
    my_table = clock.maketrans(x, y)
    return clock.translate(my_table)

# Translating numbers in name to my desired font ;D (feel free to modify it)

def name_clock_font(clock):
    x = "0123456789"
    y = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    my_table = clock.maketrans(x, y)
    return clock.translate(my_table)

async def main():
    uvloop.install()
    # Initializing a telegram session to my app

    app = Client("my_account", api_id, api_hash)

    async with app:

        while True:
            # Checking minute to change

            if round(time()) % 60 == 0:
                await asyncio.sleep(1)
                now = datetime.now(timezone('Asia/Tehran'))    # Change the 'Asia/Tehran' to your local timezone.
                # Extracting current time (hour and minutes only)

                current_time = now.strftime("%H:%M")
                hour = int(now.strftime("%H"))
                minute = int(now.strftime("%M"))


                text = current_time
                bio_text = f"『{bio_clock_font(text)}』https://alibot.ir"
                
                lastname_text = name_clock_font(text)
                
                if hour == minute:
                    # print("Lovers time <3")
                    profile_bio = f"❤️💚 | {bio_text} | 💚❤️"
                    uvloop.install()
                    await app.update_profile(bio=profile_bio, last_name=f"❤️『{lastname_text}』❤️")


                elif 00 <= hour <= 11:
                    profile_bio = f'ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌅 | {bio_text}'
                    uvloop.install()
                    await app.update_profile(bio=profile_bio, last_name=f"『{lastname_text}』")


                elif 12 <= hour <= 17:
                    profile_bio = f'ʙᴜᴇɴᴀꜱ ᴛᴀʀᴅᴇꜱ ☀ | {bio_text}'
                    uvloop.install()
                    await app.update_profile(bio=profile_bio, last_name=f"『{lastname_text}』")


                elif 18 <= hour <= 21:
                    profile_bio = f'ДОБРЫЙ ВЕЧЕР ⭐ | {bio_text}'
                    uvloop.install()
                    await app.update_profile(bio=profile_bio, last_name=f"『{lastname_text}』")

                else:
                    profile_bio = f'안녕히 주무세요 🌙 | {bio_text}'
                    uvloop.install()
                    await app.update_profile(bio=profile_bio, last_name=f"『{lastname_text}』")

                uvloop.install()
                await app.update_profile(first_name="Your name here.")
                # app.update_profile(last_name=f"『{lastname_text}』")

uvloop.install()

if __name__ == "__main__":
    asyncio.run(main())