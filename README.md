# Proyecto3-BigData

- El archivo spark.py, es el ejcutable de python exportado de jupiter, es el que es ejecutado en spark.
- El archivo S3.sh, es el srcipt que va en steps en el EMR , el encargado de ejecutar el .py y subir a s3 los png generados.
- El archivo data.sh es el script en ec2 que me toma los datos de la pagina del gobierno y me los manda a s3, tambien es encargado de clonar los clusters.
- El archivo crontab es el archivo para automatizar todo esto, me ejecuta el script data.sh todos los dias a las 10am.
- El archivo bootstrap.sh, es un archivo para configurar el cluster con librerias que necesitamos tal como el matplotlib.
- El archivo configuration.json es el archivo de configuracion del cluster para que spark me funcione con python 3.
