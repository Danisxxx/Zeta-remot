import pymongo
from pymongo import MongoClient
from datetime import datetime

class Database:
    def __init__(self):
        # URI de conexión a MongoDB
        self.uri = "mongodb://mongo:tuEfjKQoXEuBMHJASGQdgfVQFaGXPYsy@autorack.proxy.rlwy.net:38506"
        self.client = None
        self.db = None
        self.users_collection = None

    def connect(self):
        """Conecta a la base de datos y selecciona la colección de usuarios"""
        try:
            # Conexión al cliente de MongoDB
            self.client = MongoClient(self.uri)
            # Seleccionamos la base de datos
            self.db = self.client['bot_database']  # Puedes cambiar 'bot_database' por el nombre que prefieras
            # Seleccionamos la colección de usuarios
            self.users_collection = self.db['users']
            print("Conexión exitosa a la base de datos MongoDB!")
            self.create_users_collection_if_not_exists()
        except Exception as e:
            print(f"Error al conectar con MongoDB: {e}")
    
    def create_users_collection_if_not_exists(self):
        """Crea la colección 'users' si no existe y asegura que la estructura es la correcta"""
        # Verificamos si la colección 'users' está vacía
        if self.users_collection.count_documents({}) == 0:
            # Si está vacía, insertamos un documento de ejemplo
            print("Colección 'users' está vacía. Creando documentos predeterminados...")
            self.add_default_user_structure()
    
    def add_default_user_structure(self):
        """Agrega un documento por defecto para inicializar la estructura de usuarios"""
        # Este documento contiene los campos con valores predeterminados
        default_user = {
            "id": None,  # El campo 'id' está inicializado a None (null)
            "rango": "Free user",
            "dias": 0,
            "creditos": 0,
            "antispam": 90,
            "ban": "no",
            "reason": "no especificada",
            "bin_lasted": None,
            "fecha_registro": None
        }
        
        # Insertamos el documento en la colección
        self.users_collection.insert_one(default_user)
        print("Documento de usuario predeterminado insertado!")

    def add_user(self, user_id=None, rango="Free user"):
        """Agrega un nuevo usuario con el ID de Telegram"""
        user = {
            "id": user_id,  # El ID del usuario será None si no se pasa uno
            "rango": rango,
            "dias": 0,
            "creditos": 0,
            "antispam": 90,
            "ban": "no",
            "reason": "no especificada",
            "bin_lasted": None,
            "fecha_registro": datetime.now()
        }
        
        # Insertamos el nuevo usuario
        self.users_collection.insert_one(user)
        print(f"Usuario {user_id} agregado correctamente!")

    def get_user(self, user_id):
        """Obtiene la información de un usuario por su ID"""
        user = self.users_collection.find_one({"id": user_id})
        if user:
            return user
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia de la base de datos
    db = Database()
    db.connect()  # Conectar a la base de datos

    # Agregar un nuevo usuario con 'id' inicial como None
    user_id = None  # O cualquier ID que quieras agregar, si no, será None por defecto
    db.add_user(user_id)

    # Obtener el usuario recién agregado
    user = db.get_user(user_id)
    if user:
        print(f"Datos del usuario: {user}")
