import os
import pandas as pd
import csv
import gnsscal
from datetime import date

class DataFrame:
    def __init__(self, data_dict):
        self.data=pd.DataFrame(data_dict)

    def mostrar_dataframe(self):
        print(self.data)



dataframes=[]

for i in range(5):
    data_dict={'Nombre': ['Persona{}'.format(i+1), 'Persona{}'.format(i+2), 'Persona{}'.format(i+3)],
        'Edad': [25+i, 30+i, 35+i],
        'Ciudad': ['Ciudad{}'.format(i+1), 'Ciudad{}'.format(i+2), 'Ciudad{}'.format(i+3)]
    }

    df = DataFrame(data_dict)
    dataframes.append(df)


for i, df in enumerate(dataframes):
    print("DataFrame", i+1)
    df.mostrar_dataframe()
    print()