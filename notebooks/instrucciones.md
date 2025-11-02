# Instrucciones de ejecución del proyecto

Si lo único que se desea es probar el modelo a través de la API y obtener la correspondiente respuesta, se puede hacer de la siguiente manera:

1. Abrir el archivo Genetica_app.ipynb y ejecutarlo desde el entorno que se prefiera (Visual Studio Code, Jupyter, Colab, etc.).

2. Ejecutar las celdas de todos los apartados, excepto las de “Pruebas” y “Solicitud de predicción al Servidor”, que no son necesarias. Aunque, si se desea, también se pueden ejecutar.

3. Al finalizar de ejecutarlas, en la última celda del apartado llamado “Montaje servidor”, se nos mostrará un enlace referido como "URL Pública".

4. Copiar ese enlace y abrir el archivo solicitud.py para editarlo.

5. Pegar el enlace en la variable url_sola.

6. En el apartado de datos de entrada, ajustar los porcentajes genéticos a nuestro gusto.

7. Guardar los cambios en solicitud.py y ejecutarlo desde la terminal, asegurándose de que el servidor del Genetica_app.ipynb sigue activo.

8. Al ejecutar el script, se obtendrá la distancia genética y una imagen con los valores PCA plasmados en una gráfica.

Si por el contrario, se desea probar todo, el orden de ejecución es el siguiente: primero Iberian_Heritage.ipynb, luego Regresion_Genetica.ipynb, a continuación Genetica_app.ipynb y, por último, solicitud.py.

Todos los archivos necesarios para ejecutar los diferentes cuadernos se importan automáticamente conforme se ejecutan sus respectivas celdas de importación, no es necesario hacer nada más con ellos.
