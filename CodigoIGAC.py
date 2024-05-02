import os
import pandas as pd
import csv
import gnsscal

#holaaa

#Leemos un archivo con las 105 estaciones SGC, las enlistamos y convertimos los caracteres a minusculas
EstacionesIGAC=[' ',' ','ESTACIÓN']
Estacionescomp=[]

with open('EstacionesIGAC.csv', newline='') as File:
    reader=csv.reader(File)
    for fila in reader:
        EstacionesIGAC.append(fila[0])
        Estacionescomp.append(fila[0])
        EstacionesIGACmin=[elemento.lower() for elemento in Estacionescomp]

#Creamos un dataframe
tabla = pd.DataFrame(EstacionesIGAC)
#print(len(EstacionesIGAC))
#print(len(EstacionesIGACmin))


#Ingresamos el directorio
directorio='//172.26.0.20/Elite_Sub_Geografia_Cartografia/3130GITGeodesia/90RSMNReferencia/3EOContinua/9ARINEX/Rinex15s/2024'

#definimos una funcion que determina a que semana GPS pertenece el doy
def doy2GPSWeek(año,doy):
    fecha=gnsscal.yrdoy2date(año, doy)
    GPSWeek=gnsscal.date2gpswd(fecha)
    return GPSWeek




#Recorremos todas las carpetas y hacemos un listado de todas las estaciones
with os.scandir(directorio) as ficheros:
    for fichero in ficheros:
        print(fichero.name)
        #Creamos las 3 primeras filas del archivo excel que contiene vacio, semana gnss y dia gnss
        ActividadDiaria=['']
        GPSweek,DayWeek=doy2GPSWeek(2024,int(fichero.name))
        ActividadDiaria.append(GPSweek)
        ActividadDiaria.append(fichero.name)
	
	
        #Se crea una nueva ruta direc agregandole a directorio el nombre de cada fichero
        direc= os.path.join(directorio,fichero.name, '24o/V2.11')
        

#        #Se recorre la carpeta con ruta direc, comparamos los archivos existentes con EstacionesIGAC
 #       for elemento in EstacionesIGACmin:
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
        lon=len(EstacionesIGACmin)
        for i in range(0,lon):
            n=0
            for file in os.listdir(direc):
                    file_lower=file.lower()
                    #print(file_lower,"-",EstacionesIGACmin[i])
                    if file_lower.startswith(EstacionesIGACmin[i]):
                        n=n+1                    
            if n!=0:
                ActividadDiaria.append('1')
            else:
                ActividadDiaria.append('0')
        tabla[fichero.name]=ActividadDiaria
        #print(tabla)
        #print(len(ActividadDiaria))

tabla.to_csv("DatosIGAC.csv", index=False)