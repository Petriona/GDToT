import helper, traceback
from pyrogram import Client, filters

bot = Client("Bot",
   api_id=11781837,
   api_hash="4e4135898bbc89c27c656aa4aeed6021",
   bot_token="5753964641:AAHhDHJJpPf5RE_GNT09GiDwx8YqSkjWNk0"
  )

@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply("Hey, I'm Alive.") 
    
@bot.on_message(filters.command('gdtot'))
async def GDToT(bot, message):
    try:
        link = await helper.getGDToT(helper.getProperLink(message.command[1]))
        await message.reply(link)
    except Exception as e:
        await message.reply(f"**Traceback Info:**\n`{traceback.format_exc() }`\n**Error Text:**\n`{e}`")
        
print('\n\nBot Started Successfully.\n\n')
bot.run()
