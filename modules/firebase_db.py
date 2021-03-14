class DB():
    '''
        DB es una clase que contiene las funciones para un CRUD: create, read, update y delete
    '''

    def __init__(self):
        from firebase import Firebase
        self.db = Firebase.FirebaseApplication('https://desafios-page-default-rtdb.firebaseio.com/', None)

    def create(self, obj):
        resultado = self.db.post('/comments', obj)
        print(f'{resultado}')
    
    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass