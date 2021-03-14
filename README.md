# Firebase-Python
Repo test para conexión con Firebase

```cmd
pip install firebase-admin
pip install python-dotenv
```

## Lectura de datos
Para poder leer datos, conviene realizar una lectura indexada por alguna key del diccionario. Utilizo `orderByChild()` al utilizar el método `get()`. Hay que editar las reglas de la siguiente manera:
```json
{
  "rules": {
    ".read": true,
    ".write": true,
    "comments":{
      ".indexOn": ["nombre"]
    }
  }
}
```
Teniendo una colección `comments`, le indicamos con el método `.indexOn` cuales van a ser las keys que puede indexar.