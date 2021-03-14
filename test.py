from modules.firebase_db import DB

db = DB()

data = {
    'nombre': 'Naruto',
    'correo': 'nuzumaki@google.com',
    'comentario': 'Hola! estoy probando Firebase'
}

# Crear datos
# db.create('/comments', data)

# Leer datos
comments = db.read('/comments', 'nombre')
for _, comment in comments.items():
    print(f'{comment["correo"]}')

# Actualizar datos