import os



#Funcion para revisar si todos los archivos .d tienen solo rinex 2
directorio='//172.26.0.20/Elite_Sub_Geografia_Cartografia/3130GITGeodesia/90RSMNReferencia/3EOContinua/9ARINEX/Rinex15s/2024'

def Comprobaciond():
    with os.scandir(directorio) as ficheros:
        for fichero in ficheros:
            try:
                direc= os.path.join(directorio,fichero.name, '24d')
                with os.scandir(direc) as rnxs:
                    for rnx in rnxs: 
                        if rnx.name!="V2.11":
                            print(f"Carpeta {fichero.name}: {rnx.name}")
            except:
                print(f"Error en la carpeta {fichero.name}")




#definimos una funcion que lee las estaciones un dia dado en la carpeta d
def estacionesd(day):
    estaciones=[]
    try:
        direc= os.path.join(directorio,day, '24d/V2.11')
        #print(direc)
        with os.scandir(direc) as file:
            for fil in file:
                texto=fil.name[0:4]
                estaciones.append(texto.lower())
                esta=set(estaciones)
    except:
        print(f"Error en la carpeta")

    return esta


#definimos una funcion que lee las estaciones un dia dado en la carpeta .o rinex 2.11
def estacionesO2(day):
    estaciones=[]
    try:
        direc= os.path.join(directorio,day, '24o/V2.11')
        #print(direc)
        with os.scandir(direc) as file:
            for fil in file:
                texto=fil.name[0:4]
                estaciones.append(texto.lower())
                esta=set(estaciones)
    except:
        print(f"Error en la carpeta")

    return esta



#definimos una funcion que lee las estaciones un dia dado en la carpeta .o rinex 3.0
def estacionesO3(day):
    estaciones=[]
    try:
        direc= os.path.join(directorio,day, '24o/V3.0')
        #print(direc)
        with os.scandir(direc) as file:
            for fil in file:
                texto=fil.name[0:4]
                estaciones.append(texto.lower())
                esta=set(estaciones)
    except:
        print(f"Error en la carpeta")

    return esta






#Comprobamos todos los dias por la longitud
with os.scandir(directorio) as ficheros:
        for fichero in ficheros:
            try:
                ed=len(estacionesd(fichero.name))
                eo2=len(estacionesO2(fichero.name))
                eo3=len(estacionesO3(fichero.name))

                if (ed != eo2) or (ed != eo3) or (eo2 != eo3):
                    print(f"Carpeta {fichero.name}: ed={ed} - eo2={eo2} - eo3={eo3}")
                elif (ed == eo2) and (ed == eo3) and (eo2 == eo3):
                    print("IGUALESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")

            except:
                print(f"Error en la carpeta {fichero.name}")


#Comprobaciond()

#
#unicos_d_o2=ed.intersection(eo2, eo3)
#print("interseccion:",unicos_d_o2)