import requests
import base64
from io import BytesIO
from PIL import Image

url_sola = "" # Pega aquí la URL sin el /predict/

url= f"{url_sola}/predecir/"

# Datos de entrada (ajústalos como quieras teniendo en cuenta que entre los 5 sumen 100)
data = {
    "celtas": 68,
    "iberos": 30,
    "fenicios": 0,
    "griegos": 1,
    "italicos": 1
}

# Enviar petición POST
response = requests.post(url, json=data)

# Comprobar si la petición fue exitosa
if response.status_code == 200:
    resultado = response.json()
    print("Respuesta recibida correctamente:\n")
    print("Distancia G1:", resultado["distancia_g1"])
    print("PCA X:", resultado["pca_x"])
    print("PCA Y:", resultado["pca_y"])

    # Mostrar imagen desde el campo Base64
    imagen_bytes = base64.b64decode(resultado["imagen_base64"])
    imagen = Image.open(BytesIO(imagen_bytes))
    imagen.show()  # abrirá la imagen en el visor de tu sistema

else:
    print("Error:", response.status_code)
    print(response.text)