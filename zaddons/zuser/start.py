import mysql.connector
from datetime import datetime
from pyrogram import Client, filters

# Conexión a la base de datos MySQL con la contraseña directamente en el código
def connect_to_db():
    return mysql.connector.connect(
        host="autorack.proxy.rlwy.net",
        user="root",
        password="RXejfEMjKukOOsNdxIEqPNmJrKUyDEel",
        database="railway",
        port=54123
    )

# Función para crear la tabla 'users' si no existe
def create_users_table():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id BIGINT PRIMARY KEY,
            rango VARCHAR(255),
            priv INT,
            dias INT,
            creditos INT,
            antispam INT,
            ban VARCHAR(255),
            bin_lasted VARCHAR(255),
            regist DATETIME
        )
    """)
    db.commit()
    db.close()

# Función para verificar si el usuario existe en la base de datos
def user_exists(user_id):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    user = cursor.fetchone()
    db.close()
    return user

# Función para registrar al usuario si no existe
def register_user(user_id):
    db = connect_to_db()
    cursor = db.cursor()
    register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
        INSERT INTO users (id, rango, priv, dias, creditos, antispam, ban, bin_lasted, regist)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, 'Free users', 0, 0, 0, 90, 'no reason', None, register_date))
    db.commit()
    db.close()

@zeta("start")
async def help_command(client, message):
    # Crear la tabla si no existe
    create_users_table()

    user_id = message.from_user.id
    user = user_exists(user_id)

    if not user:
        # Si el usuario no existe en la base de datos, registrarlo
        register_user(user_id)

    await message.reply_text(start, reply_to_message_id=message.id)
