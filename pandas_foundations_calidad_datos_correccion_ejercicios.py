print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("******************************************")
print("CALIDAD DE DATOS - CORRECCIÓN - EJERCICIOS")
print("******************************************")

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

# - El índice debería ser el número de expediente
# - Nos importaba casi todas las variables como objeto
# - Los nombres de variables tenían acentos símbolos y espacios
# - Las 2 últimas variables no contienen información
# - Había registros duplicados
# - Teníamos muchos nulos

# Vamos a ir paso a paso. Comenzamos por corregir los nombres.
# Pásale como una lista los mismos nombres pero quitando acentos y símbolos, y todo en minúscula

cabecera = ['expediente','fecha','hora','calle','numero','distrito','tipo_accidente','tiempo','vehiculo','persona','edad','sexo','lesividad','unamed_1','unamed_2']

df = pd.read_excel("../../../00_DATASETS/2020_Accidentalidad.xlsx",
                        sheet_name = "2020_Accidentalidad",
                        index_col = "expediente",
                        header = 0,
                        names = cabecera,
                        parse_dates = ["fecha"]) # solo podemos importar por hojas (le indicamos el número de hoja o el nombre)

# na_values = ["-","DESCONOCIDA"],

# O podemos utilizar:
# from janitor import clean_names
# print(clean_names(df))

df = df.drop("unamed_1", axis = 1)
df = df.drop("unamed_2", axis = 1)

print(df)
print(df.head(2))

print("***********")
print("EJERCICIO 2")
print("***********")

# Elimina los registros duplicados

print(df)
df.drop_duplicates(inplace = True)
print(df)

print("***********")
print("EJERCICIO 3")
print("***********")

# Corrige los tipos de las variables.
# PISTA: desde distrito a sexo ambos incluídos deberían ser categóricas. El resto puedes dejarlo como está.
# Comienza revisando los tipos de datos.

print(df.info())

tipos = {'distrito':'category',
         'tipo_accidente':'category',
         'tiempo':'category',
         'vehiculo':'category',
         'persona':'category',
         'edad':'category',
         'sexo':'category'}

df = df.astype(tipos)

print(df.info())

# Una mejor solución:

# df.loc[;,"distrito":"sexo"] = df.loc[;,"distrito":"sexo"].astype("category")

print("***********")
print("EJERCICIO 4")
print("***********")

# Gestiona los nulos.

# Con el tema nulos hay que variable a variable tomando una decisión.
# Así que antes que nada vuelve a sacar el conteo de nulos por variable.

print(df.isna().sum().sort_values(ascending = False))

# Analizando la naturaleza y el conteo de cada variable podríamos llegar las siguientes conclusiones:

# - En numero y distrito son solo 2 nulos: eliminar nulos
# - tipo_persona, tipo_accidente y tipo_vehiculo tienen pocos nulos y podemos imputarlos por la moda
# - En el sexo y estado_metereológico vamos a crear una categoría "Desconocido"
# - En lesividad, a diferencia de las anteriores podría ser que no hubo lesión en ese accidente, así que sustituiremos por cero
# - Acuérdate de ir guardando en df en cada paso.

# Eliminar nulos en 'numero' y 'distrito'
df = df.dropna(subset=['numero', 'distrito'])

# Imputar nulos en 'tipo_persona', 'tipo_accidente' y 'tipo_vehiculo' con la moda
for column in ['persona', 'tipo_accidente', 'vehiculo']:
    df[column].fillna(df[column].mode()[0], inplace=True)

# Crear una categoría "Desconocido" para nulos en 'sexo' y 'estado_metereológico'

df["sexo"] = df.sexo.cat.add_categories('Desconocido')
df["tiempo"] = df.tiempo.cat.add_categories('Desconocido')

for column in ['sexo', 'tiempo']:
    df[column].fillna('Desconocido', inplace=True)

print(df.sexo.value_counts(ascending = False))
print(df.tiempo.value_counts(ascending = False))

# Sustituir nulos en 'lesividad' con cero
df['lesividad'].fillna(0, inplace=True)

print(df)
print(df.head(2))
print(df.info())

print("***********")
print("EJERCICIO 5")
print("***********")

# Vuelve a sacar el conteo de nulos para comprobar que todo es correcto:

print(df.value_counts(dropna=False)) # conteo de Status incluyendo nulos

print(df[df.duplicated()])
print(df[df.duplicated(keep = False)])

# Haz un análisis de nulos a ver cuantos tenemos por variable.

print(df.isna().sum().sort_values(ascending = False))


