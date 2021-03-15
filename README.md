# Firebase-Python 🔥🐍
Repositorio para mostrar manejo básico de Firebase. Guía utilizada: [How to Get Started with Firebase Using Python - freeCodeCamp](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/).

## Librerías
```cmd
pip install firebase-admin
pip install python-dotenv
```

## .env
En la ruta del proyecto, hay que crear un archivo `.env` e ingresar las siguientes variables de entorno:
```bash
GOOGLE_APPLICATION_CREDENTIALS = <Path del json con credenciales de la DB>
URL_DATABASE = <URL de la DB>
```

## Indexación de datos
Para poder realizar una búsqueda en la DB de Firebase, debemos utilizar el método `orderByChild()`. En la documentación nos pide que realicemos una indezación de los valores que deseemos utilizar para las referencias en la búsqueda de algún dato de interés. Para esto, debemos editar las reglas de la DB de la siguiente manera:
```json
{
  "rules": {
    ".read": true,
    ".write": true,
    "comments":{
      ".indexOn": ["nombre", "correo"]
    }
  }
}
```
Teniendo una colección `comments`, le indicamos con el método `.indexOn` cuales van a ser los valores que puede indexar. Los métodos `.read` y `.write` están como `true` para que podamos realizar consultas (si no, no podemos leer, editar, crear o eliminar datos).
Todo esto está explicado al detalle en la [documentación](https://firebase.google.com/docs/database/admin/start).