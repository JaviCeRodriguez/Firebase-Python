import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
from dotenv import load_dotenv
class DB():
    '''
        DB es una clase que contiene las funciones para un CRUD: create, read, update y delete
    '''
    def __init__(self):
        load_dotenv()
        CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        URL_DB = os.getenv("URL_DATABASE")

        cred_obj = credentials.Certificate(CREDENTIALS)
        firebase_admin.initialize_app(cred_obj, {
            'databaseURL':URL_DB
            })
        

    def create(self, path: str, obj: dict):
        '''
        Crear nuevo objeto en un path específico de Realtime Database. Ejemplo:\n
        path: "/comments"\n
        obj: {"name": "Naruto", "comment": "Seré el Hokage!"}
        '''
        ref = db.reference(path)
        ref.push().set(obj)
    
    def read(self, path: str, order: str):
        '''
        Leer un objeto en documento almacenado en Realtime Database.\n
        Buscar en un "path" específico y con un "order" por child del path.\n
        Editar las reglas para poder indexar utilizando "order".
        '''
        ref = db.reference(path)
        return ref.order_by_child(order).get()
    
    def update(self):
        pass
    
    def delete(self):
        pass