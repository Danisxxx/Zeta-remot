from configs._def_main_ import *  

@zeta("help")  
async def help_command(client, message):
    await message.reply_text(help,
        reply_to_message_id=message.id
    )
