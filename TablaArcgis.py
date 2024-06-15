import os
import pandas as pd
import openpyxl
import csv
import gnsscal



#Ingresamos los directorios de matrices
directorio="C:/Users/Paola.galindo/Documents/story map/Codigos/MatrizActivas/Estadoestaciones.xlsx"
DirSalida="C:/Users/Paola.galindo/Documents/story map/Codigos/MatrizActivas/tabla.xlsx"


# Leemos el archivo excel con multiples hojas
DF = pd.ExcelFile(directorio)

# Guardamos los nombres de las hojas en una variable, luego leemos cada hoja y las guardamos como un dataframe. Los dataframe estan almacenados en una biblioteca
Hojas_DF = DF.sheet_names
dfs = {name: DF.parse(name) for name in Hojas_DF}

#Reducimos los dataframe a solo la estacion y estado
columns_to_keep = [0, 'Estado']
Red = {name: df[columns_to_keep] for name, df in dfs.items()}


#Renombramos la columna estado por estado + mes IGAC, y eliminamos los encabezados
for name,df in Red.items():
    df=df.rename(columns={'Estado': f'Estado {name}'})
    df=df.rename(columns={None: 'Estacion'})
    df.drop([0,1,2], axis=0, inplace=True)
    Red[name]=df



def Tablatodoslosmeses():

    #Inicializamos un Dataframe para unir los dataframe 
    merged=Red['Mes 01']

    for name, df in Red.items():
        if name !='Mes 01':
            merged=pd.merge(merged,df, on=0, how='outer')
    
    merged.to_excel(DirSalida, index=False)


Tablatodoslosmeses()