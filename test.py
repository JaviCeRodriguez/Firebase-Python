from modules.firebase_db import DB

data = {
    'nombre': 'Javo',
    'edad': 25
}

DB().create(data)