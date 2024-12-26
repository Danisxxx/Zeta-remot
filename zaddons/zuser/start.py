from configs._def_main_ import *
from pymongo import MongoClient
from datetime import datetime

# Conexión a MongoDB (conexión pública)
client = MongoClient("mongodb://mongo:tuEfjKQoXEuBMHJASGQdgfVQFaGXPYsy@autorack.proxy.rlwy.net:38506")
db = client["my_database_name"]  # Aquí es el nombre de tu base de datos
users_collection = db["users"]  # Aquí es la colección 'users' dentro de la base de datos

@zeta("start")
async def help_command(client, message):
    # Obtener el ID del usuario de Telegram
    user_id = message.from_user.id

    # Comprobar si el usuario ya está en la base de datos
    user = users_collection.find_one({"id": user_id})

    if user is None:
        # Si no existe, crear un nuevo registro para el usuario
        new_user = {
            "id": user_id,
            "rango": "Free user",
            "dias": 0,
            "creditos": 0,
            "antispam": 90,
            "ban": "no",
            "reason": "no especificada",
            "bin_lasted": None,
            "fecha_registro": datetime.now()  # Fecha de registro actual
        }
        users_collection.insert_one(new_user)
        await message.reply_text("¡Bienvenido! Tu cuenta ha sido creada.",
                                  reply_to_message_id=message.id)
    else:
        # Si ya existe, puedes actualizar el campo `fecha_registro` o cualquier otro
        users_collection.update_one(
            {"id": user_id},
            {"$set": {"fecha_registro": datetime.now()}}  # Solo actualiza la fecha de registro
        )
        await message.reply_text("¡Bienvenido de nuevo! Tu cuenta ya está registrada.",
                                  reply_to_message_id=message.id)
