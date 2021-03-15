# Firebase-Python 🔥🐍
Repo test para conexión con Firebase

```cmd
pip install firebase-admin
pip install python-dotenv
```

## .env
En la ruta del proyecto, hay que crear un archivo `.env` e ingresar las siguientes variables de entorno:
```
GOOGLE_APPLICATION_CREDENTIALS = <Path del json con credenciales de la DB>
URL_DATABASE = <URL de la DB>
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