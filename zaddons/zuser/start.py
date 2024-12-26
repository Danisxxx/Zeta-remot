from configs._def_main_ import *  

@zeta("start")
async def help_command(client, message):
    # Crear la tabla si no existe
    create_users_table()

    user_id = message.from_user.id
    user = user_exists(user_id)

    if not user:
        # Si el usuario no existe en la base de datos, registrarlo
        register_user(user_id)

    await message.reply_text("¡Bienvenido al bot!", reply_to_message_id=message.id)
