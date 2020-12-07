from pyspark.sql import SparkSession
import boto3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from operator import itemgetter
from itertools import islice
from datetime import datetime

spark=SparkSession.builder.appName('data_processing').getOrCreate()

df=spark.read.csv('s3://proyecto-big-data-jsj/datos/'+datetime.now().strftime('%d-%m')+'.csv',inferSchema=True,header=True)

df_new=df.drop('Fecha de notificación','ID de caso', 'Tipo de contagio','fecha reporte web', 'Código DIVIPOLA departamento', 'Código DIVIPOLA municipio', 'Código ISO del país', 'Pertenencia étnica', 'Nombre del grupo étnico' ,'Ubicación del caso', 'Estado', 'Unidad de medida de edad', 'Fecha de diagnóstico', 'Tipo de recuperación','Fecha de recuperación','Fecha de inicio de síntomas','Fecha de muerte')

fallecido_dpto=df_new.filter(df_new['Recuperado']=='Fallecido').groupBy('Nombre departamento').count()

fallecido_edad=df_new.filter(df_new['Recuperado']=='Fallecido').groupBy('Edad').count()

fallecido_sexo_dpto=df_new.filter(df_new['Recuperado']=='Fallecido').groupBy('Sexo','Nombre departamento').count()

fallecido_pais=df_new.filter(df_new['Recuperado']=='Fallecido').groupBy('Nombre del país').count()

array_fd1=np.array(fallecido_dpto.select('Nombre departamento','count').collect())

tmp = []
for x in array_fd1:
    tmp.append([x[0],int(x[1])])

Dpt = sorted(tmp, key=lambda x: x[1] ,reverse=True)


plt.figure(figsize=(20,10))
plt.xlabel('Muertes')
plt.title('Departamentos con mas muertes')
for x in islice(Dpt, 0, 10):
    plt.barh(x[0],x[1])
plt.savefig('/home/hadoop/muertes_departamento.png')    


array_fe=np.array(fallecido_edad.select('Edad','count').collect())

tmp = []
for x in array_fe:
    tmp.append([str(x[0]),x[1]])


Edad = sorted(tmp, key=lambda x: x[1] ,reverse=True)

plt.figure(figsize=(20,10))
plt.ylabel('Muertes')
plt.xlabel('Edad')
plt.title('Poblacion Vulnerable')

for x in islice(Edad, 0, 20):
      plt.bar(x[0],x[1])
plt.savefig('/home/hadoop/muertes_edad.png')    



array_fs=np.array(fallecido_sexo_dpto.select('Sexo','nombre departamento','count').collect())

tmp = []
mujeres = []
hombres =[]
dpto =[]
for x in array_fs:
    tmp.append([x[0],x[1],int(x[2])])
    
Sexo = sorted(tmp, key=lambda x: x[2],reverse=True)
tmp.clear()

for x in Sexo:
    if x[1] =='ANTIOQUIA' or x[1] =='BOGOTA' or x[1] =='VALLE' or x[1] =='BARRANQUILLA':
        tmp.append(x)

Muertes = sorted(tmp, key=lambda x: x[1],reverse=True)

for x in Muertes:
    
    if x[0] == 'M' :
        hombres.append(x[2])
    else:
        mujeres.append(x[2])
        dpto.append(x[1])

x = np.arange(len(dpto))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10,10),dpi=150)
rects1 = ax.bar(x - width/2, hombres, width, label='Hombres')
rects2 = ax.bar(x + width/2, mujeres, width, label='Mujeres')

ax.set_ylabel('Muertes')
ax.set_title('Muertes por genero en departamentos importantes')
ax.set_xticks(x)
ax.set_xticklabels(dpto)
ax.legend()

plt.savefig('/home/hadoop/muertes_genero.png')  




array_fp=np.array(fallecido_pais.select('Nombre del país','count').collect())

tmp = []
for x in array_fp:
    if x[0] != None:
        tmp.append([x[0],int(x[1])])
        
Pais = sorted(tmp, key=lambda x: x[1] ,reverse=True)


plt.figure(figsize=(20,10))
plt.xlabel('Muertes')
plt.title('Extrangeros que han muerto')
for x in islice(Pais, 0, 10):
    plt.barh(x[0],x[1])
plt.savefig('/home/hadoop/muertes_extrangeros.png')  




