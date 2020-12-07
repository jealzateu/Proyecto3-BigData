#!/bin/bash
aws s3 cp s3://proyecto-big-data-jsj/spark.py /home/hadoop/
spark-submit /home/hadoop/spark.py
aws s3 cp /home/hadoop/muertes_departamento.png s3://proyecto-big-data-jsj/graficas/"`date +"%d-%m"`"/
aws s3 cp /home/hadoop/muertes_edad.png s3://proyecto-big-data-jsj/graficas/"`date +"%d-%m"`"/
aws s3 cp /home/hadoop/muertes_genero.png s3://proyecto-big-data-jsj/graficas/"`date +"%d-%m"`"/
aws s3 cp /home/hadoop/muertes_extrangeros.png s3://proyecto-big-data-jsj/graficas/"`date +"%d-%m"`"/


