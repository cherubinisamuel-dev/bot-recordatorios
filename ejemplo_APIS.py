import requests

# 1. Dirección de una API pública que devuelve datos de un usuario de prueba
url = "https://api.github.com/users/octocat"

# 2. Hacemos la petición de tipo GET (pedir información)
respuesta = requests.get(url)

# 3. Revisamos el código de estado HTTP (200 significa "OK / Éxito")
print("Código de estado:", respuesta.status_code)

# 4. Transformamos el texto JSON recibido en un Diccionario de Python
datos = respuesta.json()

# 5. Extraemos información del diccionario igual que en tus proyectos anteriores
print(datos.keys())