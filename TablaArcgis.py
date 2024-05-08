import os
import pandas as pd
import openpyxl
import csv
import gnsscal



#Ingresamos los directorios de matrices del IGAC y del SGC
directorio="C:/Users/hp/Documents/Documento/IGAC/Depuración/MatrizActivas/EstadoestacionesIGAC.xlsx"
directorio2='C:/Users/hp/Documents/Documento/IGAC/Depuración/MatrizActivas/EstadoestacionesSGC.xlsx'


# Leemos el archivo excel con multiples hojas
DFIgac = pd.ExcelFile(directorio)
DFSgc = pd.ExcelFile(directorio2)

# Guardamos los nombres de las hojas en una variable, luego leemos cada hoja y las guardamos como un dataframe. Los dataframe estan almacenados en una biblioteca
Hojas_DFIgac = DFIgac.sheet_names
Hojas_DFSgc = DFSgc.sheet_names
dfsIgac = {name: DFIgac.parse(name) for name in Hojas_DFIgac}
dfsSgc = {name: DFSgc.parse(name) for name in Hojas_DFSgc}

#Reducimos los dataframe a solo la estacion y estado
columns_to_keep = [0, 'Estado']
Igac_red = {name: df[columns_to_keep] for name, df in dfsIgac.items()}
SGC_red = {name: df[columns_to_keep] for name,df in dfsSgc.items()}



#Renombramos la columna estado por estado + mes IGAC, y eliminamos los encabezados
for name,df in Igac_red.items():
    df=df.rename(columns={'Estado': f'Estado {name}'})
    df=df.rename(columns={None: 'Estacion'})
    df.drop([0,1,2], axis=0, inplace=True)
    Igac_red[name]=df

#Renombramos la columna estado por estado + mes SGC y eliminamos los encabezados
for name,df in SGC_red.items():
    df=df.rename(columns={'Estado': f'Estado {name}'})
    df=df.rename(columns={None: 'Estacion'})
    df.drop([0,1,2], axis=0, inplace=True)
    SGC_red[name]=df



def Tablatodoslosmeses():

    #Inicializamos un Dataframe para unir los dataframe del IGAC
    merged_Igac=Igac_red['Mes 01']

    for name, df in Igac_red.items():
        if name !='Mes 01':
            merged_Igac=pd.merge(merged_Igac,df, on=0, how='outer')
    
    #merged_Igac.to_excel("C:/Users/hp/Documents/Documento/IGAC/Depuración/MatrizActivas/tablaIGAC.xlsx", index=False)


    #Inicializamos un Dataframe para unir los dataframe del SGC
    merged_SGC=SGC_red['Mes 01']

    for name, df in SGC_red.items():
        if name !='Mes 01':
            merged_SGC=pd.merge(merged_SGC,df, on=0, how='outer')

    #merged_SGC.to_excel("C:/Users/hp/Documents/Documento/IGAC/Depuración/MatrizActivas/tablaSGC.xlsx", index=False)

    TablaArcgis=pd.concat([merged_Igac,merged_SGC])
    TablaArcgis.to_excel("C:/Users/hp/Documents/Documento/IGAC/Depuración/MatrizActivas/tabla.xlsx", index=False)





Tablatodoslosmeses()