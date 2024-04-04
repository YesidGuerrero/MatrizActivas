import os
import pandas as pd
import csv
import gnsscal

#Leemos un archivo con las 105 estaciones SGC, las enlistamos y convertimos los caracteres a minusculas
EstacionesSGC=[' ',' ','ESTACIÓN']
Estacionescomp=[]

with open('EstacionesSGC.csv', newline='') as File:
    reader=csv.reader(File)
    for fila in reader:
        EstacionesSGC.append(fila[0])
        Estacionescomp.append(fila[0])
        EstacionesSGCmin=[elemento.lower() for elemento in Estacionescomp]

#Creamos un dataframe
tabla = pd.DataFrame(EstacionesSGC)
#print(len(EstacionesSGC))
#print(len(EstacionesSGCmin))


#Ingresamos el directorio
directorio='/Users/hp/Documents/Documento/IGAC/Depuración/1'

#definimos una funcion que determina a que semana GPS pertenece el doy
def doy2GPSWeek(año,doy):
    fecha=gnsscal.yrdoy2date(año, doy)
    GPSWeek=gnsscal.date2gpswd(fecha)
    return GPSWeek




#Recorremos todas las carpetas y hacemos un listado de todas las estaciones
with os.scandir(directorio) as ficheros:
    for fichero in ficheros:

        #Creamos las 3 primeras filas del archivo excel que contiene vacio, semana gnss y dia gnss
        ActividadDiaria=['']
        GPSweek,DayWeek=doy2GPSWeek(2024,int(fichero.name))
        ActividadDiaria.append(GPSweek)
        ActividadDiaria.append(fichero.name)

        #Se crea una nueva ruta direc agregandole a directorio el nombre de cada fichero
        direc= os.path.join(directorio,fichero.name)



#        #Se recorre la carpeta con ruta direc, comparamos los archivos existentes con EstacionesSGC
 #       for elemento in EstacionesSGCmin:
 #           #print("estacion:", elemento)
 #           #print(fichero.name)
 #           #print(ActividadDiaria)
#
#            with os.scandir(direc) as files:
#                for file in files:
#                    file_lower=file.name.lower()
#
#                    if file_lower.startswith(elemento):
#                        ActividadDiaria.append('1')
#                        break
#                    else:
#                        ActividadDiaria.append('0')
#                        break
        lon=len(EstacionesSGCmin)
        for i in range(0,lon):
            n=0
            for file in os.listdir(direc):
                    file_lower=file.lower()
                    #print(file_lower,"-",EstacionesSGCmin[i])
                    if file_lower.startswith(EstacionesSGCmin[i]):
                        n=n+1
                    #print("n:",n)
            if n!=0:
                ActividadDiaria.append('1')
            else:
                ActividadDiaria.append('0')
        tabla[fichero.name]=ActividadDiaria
        #print(tabla)
        #print(len(ActividadDiaria))

tabla.to_csv("Datos.csv", index=False)
print(tabla)