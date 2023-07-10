print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("*****************************")
print("CALIDAD DE DATOS - EJERCICIOS")
print("*****************************")

import pandas as pd
import numpy as np 

# Documentación de Pandas https://pandas.pydata.org/pandas-docs/stable/reference/index.html

print(pd.options.display.min_rows) # por defecto muestra 10 (5 superiores y 5 inferiore)

# %config IPCompleter.greedy = True # para autocompletar cuando trabajamos con notebook
pd.options.display.min_rows = 6 # por defecto nos muestra 6 registros
print(pd.options.display.min_rows)

# Estos ejercicios consisten en analizar la calidad de datos de un dataset que contiene los accidentes de tráfico en Madrid durante 2020.
# Está en Excel, se llama 2020_Accidentalidad.xlsx.

print("***********")
print("EJERCICIO 1")
print("***********")

# Importa el archivo en el objeto df y visualizalo por pantalla.

df = pd.read_excel("../../../00_DATASETS/2020_Accidentalidad.xlsx", sheet_name = "2020_Accidentalidad", index_col = "Nº  EXPEDIENTE",
                              parse_dates = ["FECHA"]) # solo podemos importar por hojas (le indicamos el número de hoja o el nombre)
print(df.head(2))
df.info()

# Algunas conclusiones sobre la importación:

# - Coge bien los nombres de variables, tienen acentos y símbolos así que nos interesa cambiarlos
# - La mayoría de variables se han importado como objeto
# - El número del expediente debería ser el índice. 

# Vamos a ir paso a paso. Comenzamos por corregir los nombres.
# Pásale como una lista los mismos nombres pero quitando acentos y símbolos, y todo en minúscula

cabecera = ['expediente','fecha','hora','calle','numero','distrito','tipo_accidente','tiempo','vehiculo','persona','edad','sexo','lesividad','unamed_1','unamed_2']

df = pd.read_excel("../../../00_DATASETS/2020_Accidentalidad.xlsx",
                        sheet_name = "2020_Accidentalidad",
                        index_col = "expediente",
                        header = 0,
                        names = cabecera,
                        na_values = ["-","DESCONOCIDA"],
                        parse_dates = ["fecha"]) # solo podemos importar por hojas (le indicamos el número de hoja o el nombre)

df = df.drop("unamed_1", axis = 1)
df = df.drop("unamed_2", axis = 1)

print(df)
print(df.head(2))

print("***********")
print("EJERCICIO 2")
print("***********")

# ¿Cuanto espacio en memoria está ocupando este dataset?

df.info(memory_usage = "deep")

print("***********")
print("EJERCICIO 3")
print("***********")

# ¿Cuantas filas y columnas tiene?

print(df.shape)

print("***********")
print("EJERCICIO 4")
print("***********")

# ¿Tiene índice ya asignado?¿O es el automático?

print(df.index) # es automático. En este ejemplo he asignado el número de expendiente

print("***********")
print("EJERCICIO 5")
print("***********")

# Extrae los nombres de las variables como una lista

print(df.columns.to_list())

print("***********")
print("EJERCICIO 6")
print("***********")

# Como la mayoría son objetos haz una visión global de estadísticos que incluya solo las tipo objeto

print(df.describe(include = ["O"]).T) # o solo incluye los objetos

print("***********")
print("EJERCICIO 7")
print("***********")

# Comprueba si hay algún duplicado en el dataset

print(df[df.duplicated()])
print(df[df.duplicated(keep = False)])

# print(df[df.duplicated()].expediente.value_counts())

print("***********")
print("EJERCICIO 8")
print("***********")

# ¿Cual es la calle en la que ha habido más accidentes?

print(df.calle.mode())

print("***********")
print("EJERCICIO 9")
print("***********")

# Haz un análisis de nulos a ver cuantos tenemos por variable.

print(df.isna().sum().sort_values(ascending = False))

print("************")
print("EJERCICIO 10")
print("************")

# Calcula el máximo, minimo, media y mediana de LESIVIDAD

print(df["lesividad"].mean())
print(df["lesividad"].median())
print(df["lesividad"].max())
print(df["lesividad"].min())
