from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


app.run()
import asyncio
from pyrogram import Client

api_id = 10248430
api_hash = "42396a6ff14a569b9d59931643897d0d"

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

asyncio.run(main())
pip3 install -U pyrogram
pip3 install -U pyrogram tgcrypto
pip3 install -U https://github.com/pyrogram/pyrogram/archive/master.zip
>>> import pyrogram
>>> pyrogram.__version__
'x.y.z'
