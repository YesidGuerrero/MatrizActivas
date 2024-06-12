import os
import pandas as pd
import csv
import gnsscal


#Leemos un archivo con las 123 estaciones IGAC, las enlistamos y convertimos los caracteres a minusculas
EstacionesIGAC=[' ',' ','ESTACIÓN']
Estacionescomp=[]

with open('C:/Users/Paola.galindo/Documents/story map/Codigos/MatrizActivas/EstacionesIGAC.csv', newline='') as File:
    reader=csv.reader(File)
    for fila in reader:
        EstacionesIGAC.append(fila[0])
        Estacionescomp.append(fila[0])
        EstacionesIGACmin=[elemento.lower() for elemento in Estacionescomp]




#Ingresamos el directorio
directorio='//172.26.0.20/Elite_Sub_Geografia_Cartografia/3130GITGeodesia/90RSMNReferencia/3EOContinua/9ARINEX/Rinex15s/2024'



#definimos una funcion que determina a que semana GPS pertenece el doy
def doy2GPSWeek(año,doy):
    fecha=gnsscal.yrdoy2date(año, doy)
    GPSWeek=gnsscal.date2gpswd(fecha)
    mes=fecha.strftime('%m')
    return GPSWeek, mes



#Creacion de array dataframes para meses disponibles hasta el momento, se crea una funcion que genera los dataframe para cada mes.
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
    df=pd.DataFrame(EstacionesIGAC)
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
                direcd= os.path.join(directorio,fichero.name,"24d/V2.11")
                direco2= os.path.join(directorio,fichero.name,"24o/V2.11")
                direco3= os.path.join(directorio,fichero.name,"24o/V3.0")

                
                lon=len(EstacionesIGACmin)
                for i in range(0,lon):
                    n=0
                    try:
                        for file in os.listdir(direcd):
                                file_lower=file.lower()
                                #print(file_lower,"-",EstacionesSGCmin[i])
                                if file_lower.startswith(EstacionesIGACmin[i]):
                                    n=n+1 
                    except:
                        print(f"La carpeta {file} no tiene .d")   

                    try:

                        for file in os.listdir(direco2):
                                file_lower=file.lower()
                                #print(file_lower,"-",EstacionesSGCmin[i])
                                if file_lower.startswith(EstacionesIGACmin[i]):
                                    n=n+1  
                    except:     
                        print(f"La carpeta {file} no tiene .O 2.11")             


                    try:
                        for file in os.listdir(direco3):
                                file_lower=file.lower()
                                #print(file_lower,"-",EstacionesSGCmin[i])
                                if file_lower.startswith(EstacionesIGACmin[i]):
                                    n=n+1    
                    except:
                        print(f"La carpeta {file} no tiene .O 3.00")

                    if n!=0:
                        ActividadDiaria.append('1')
                    else:
                        ActividadDiaria.append('0')



                df[fichero.name]=ActividadDiaria 








#Realizamos el conteo y generamos la columna de inactividad
writer = pd.ExcelWriter('C:/Users/Paola.galindo/Documents/story map/Codigos/MatrizActivas/EstadoestacionesIGAC.xlsx')
for ind, df in enumerate(data_frames):
    TotalRinex=["Total Rinex", " ", " "]
    Estado=["Estado"," "," "]
    for i in range (3,df.shape[0]):
        suma=0
        for j in range (1,df.shape[1]):
            suma=suma+int(df.iloc[i,j])
        TotalRinex.append(suma)
        if suma==0:
            est="Inactiva"
        else:
            est="Activa"
        Estado.append(est)
    df["Total"]=TotalRinex
    df["Estado"]=Estado
    #print(df)
    df.to_excel(writer,  sheet_name=f'Mes 0{ind+1}', index=False)

writer._save()