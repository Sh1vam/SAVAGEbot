#credits to @kraken_the_badass
#beautification credits to @sensei_nex for @senseiMAXprojects

#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

# uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/44fc011c221af59131761.jpg"
pm_caption = "➥ **💥🅻🅴🅶🅴🅽🅳 𝔹𝕆𝕋💥 IS:** `ONLINE`\n\n"
pm_caption += "➥ **👺🐚  т𝓔ˡ𝕖ţ𝐡𝕆Ⓝ 𝐕𝓔ŘsⓘØᑎ  👊♢:** `1.18.0` \n"
pm_caption += "➥ **🄿🅈🅃🄷🄾🄽 ♡☞:** `3.7.4` \n"
pm_caption += "➥ **👊  𝔡𝔞t𝓪в𝓪ⓢέ  𝕊𝕥𝕒𝕥𝕦𝕤  ♗:**  `Functional`\n"
pm_caption += f"➥ **//💥  ✎  𝓂𝕪 βỖⓈş  ☞  💀//** \n {DEFAULTUSER} \n"

pm_caption += "➥ **♕♟  𝕃𝕚𝕔𝕖𝕟𝕤𝕖 ♟♕** : [GNU General Public License v3.0](github.com/TeamLEGENDX/LegendBOT/blob/master/LICENSE)\n"
pm_caption += " ♕  ⓜ𝕪 𝓒𝓗𝓐𝓝𝓝𝓔𝓛  ♕ 😎 \n [CHANNEL](https://t.me/hackerget0)\n\n"
pm_caption += " Ⓜ️𝓎 ℂＲ𝑒Ａ𝕋Øⓡ 😎 \n [LEGEND X](https://t.me/legendx22)\n\n"
pm_caption += " 𝑀𝒴 𝒢𝑅❁𝒰� 😎 \n [GROUP](https://t.me/teamishere)\n"
pm_caption += "[🇮🇳 Deploy LEGEND SUPER  BOT 🇮🇳](https://github.com/legendx22/LegendBOT)"


@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
