from modules.firebase_db import DB

db = DB()

data = {
    'nombre': 'Naruto',
    'correo': 'nuzumaki@google.com',
    'comentario': 'Hola! estoy probando Firebase'
}

# Crear datos
db.create(path='/comments', obj=data)

# Leer datos
datos = db.read(path='/comments', order='nombre')
for _, comment in datos:
    print(f'{comment["correo"]}')

# Actualizar datos
db.update(path='/comments', keyIndex="nombre", keyAim="correo", valueIndex="Javo", valueAim="jcrodriguez@gmail.com")

# Eliminar datos
db.delete(path='/comments', keyIndex="correo", valueIndex="jcrodriguez@google.com")