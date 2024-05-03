import os
import pandas as pd
import csv
import gnsscal


#Ingresamos el directorio
directorio='//172.26.0.20/Elite_Sub_Geografia_Cartografia/3130GITGeodesia/90RSMNReferencia/3EOContinua/9ARINEX/Rinex_15s_SGC/OBS/2024'


#Leemos un archivo con las 105 estaciones SGC, las enlistamos y convertimos los caracteres a minusculas
EstacionesSGC=[' ',' ','ESTACIÓN']
Estacionescomp=[]

with open('EstacionesSGC.csv', newline='') as File:
    reader=csv.reader(File)
    for fila in reader:
        EstacionesSGC.append(fila[0])
        Estacionescomp.append(fila[0])
        EstacionesSGCmin=[elemento.lower() for elemento in Estacionescomp]




#definimos una funcion que determina a que semana GPS pertenece el doy
def doy2GPSWeek(año,doy):
    fecha=gnsscal.yrdoy2date(año, doy)
    GPSWeek=gnsscal.date2gpswd(fecha)
    mes=fecha.strftime('%m')
    return GPSWeek, mes



#Creacion de array dataframes para meses disponibles hasta el momento funcion que genera los dataframe para cada mes
Meses=[]
def MesesDisponibles():
    with os.scandir(directorio) as ficheros:
        for fichero in ficheros:
            n=0
            fecha=gnsscal.yrdoy2date(2024, int(fichero.name))
            mont=fecha.strftime('%m')
            for mes in Meses:
                if mont == mes:
                    n=n+1
            if n==0:
                Meses.append(mont)
    return

MesesDisponibles()

#Creamos los dataframe para cada mes
print(Meses)
data_frames=[]

for mes in Meses:
    df=pd.DataFrame(EstacionesSGC)
    data_frames.append(df)
    with os.scandir(directorio) as ficheros:
        for fichero in ficheros:
            GPSW, Mon=doy2GPSWeek(2024,int(fichero.name))
            if (mes==Mon):
                #Creamos las 3 primeras filas del archivo excel que contiene vacio, semana gnss y dia gnss
                ActividadDiaria=[fichero.name]
                ActividadDiaria.append(GPSW)
                ActividadDiaria.append(Mon)

                #Se crea una nueva ruta direc agregandole a directorio el nombre de cada fichero
                direc= os.path.join(directorio,fichero.name)


                lon=len(EstacionesSGCmin)
                for i in range(0,lon):
                    n=0
                    for file in os.listdir(direc):
                            file_lower=file.lower()
                            #print(file_lower,"-",EstacionesSGCmin[i])
                            if file_lower.startswith(EstacionesSGCmin[i]):
                                n=n+1                    
                    if n!=0:
                        ActividadDiaria.append('1')
                    else:
                        ActividadDiaria.append('0')
                df[fichero.name]=ActividadDiaria
    df.to_csv(f"Mes{mes}.csv", index=False)




# Mostramos los dataframes
for i, df in enumerate(data_frames):
    print(f"DataFrame Mes {i+1}:")
    #print(df.iloc[4])
    #print(df.iloc[:,4])
    print(df)