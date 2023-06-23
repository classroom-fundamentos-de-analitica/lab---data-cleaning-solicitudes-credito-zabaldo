"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from re import match
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)

    df=df.dropna()
    header = ['sexo','tipo_de_emprendimiento','idea_negocio','barrio','línea_credito']
    for a in header:
      df[a]=df[a].apply(lambda x: x.lower().replace("-"," ").replace("_"," "))  
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    df['monto_del_credito']=df['monto_del_credito'].apply(lambda x: x.strip("$").replace(",","")).astype(float)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce').fillna(
    pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/%d', errors='coerce'))
    df = df.drop_duplicates()
    return df