from modules.firebase_db import DB

db = DB()

data = {
    'nombre': 'Naruto',
    'correo': 'nuzumaki@google.com',
    'comentario': 'Hola! estoy probando Firebase'
}

db.create('/comments', data)