print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("******************************")
print("CALIDAD DE DATOS - DIAGNOSTICO")
print("******************************")

import pandas as pd
import numpy as np 

# Documentación de Pandas https://pandas.pydata.org/pandas-docs/stable/reference/index.html

print(pd.options.display.min_rows) # por defecto muestra 10 (5 superiores y 5 inferiore)

# %config IPCompleter.greedy = True # para autocompletar cuando trabajamos con notebook
pd.options.display.min_rows = 6 # por defecto nos muestra 6 registros
print(pd.options.display.min_rows)

df = pd.read_csv("../../../00_DATASETS/DataSetKivaCreditScoring.csv", sep = ";", index_col = "id",
					parse_dates = ["Funded Date","Paid Date"])

print(df.head(2))

# CREAR UNA MUESTRA

# No es recomendable crear una muestra para la fase de calidad de datos. Pero sí es una técnica importante a conocer para fases posteriorres.

# sample()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html

# Parámetros más importantes:

# - n: tamaño de la muestra en absoluto
# - frac: tamaño de la muestra en porcentaje
# - replace: si se admite reemplazamiento (teoría de probabilidad, que no salga otra vez el mismo registro si ya ha salido) o no. Por defecto es False
# - random_state: establecer una semilla reproducible

muestra = df.sample(n = 100)
print(muestra.shape)

# VISION GLOBAL

# Información general del dataset

# info()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html

# Parámetros más importantes:

# - memory_usage = por defecto nos da una estimación del tamaño en memoria. Si ponemos 'deep' nos da el valor real.

df.info(memory_usage = "deep")

# DIMENSIÓN DEL DATASET
# shape() nos da el número de filas y columnas

print(df.shape)

# INFORMACIÓN DEL ÍNDICE
# index() nos da el tipo de índice, el número de registros y una muestra

print(df.index)

# Si solo queremos extraer los valores, usamos values:
print(df.index.values)

# INFORMACIÓN DE LAS COLUMNAS
# columns() nos da los nombres de las columnas

print(df.columns)

# Si solo queremos extraer los valores, usamos values:
print(df.columns.values)

# O si los queremos como lista que muchas veces será más manejable usamos columns.to_list()
print(df.columns.to_list())

# TIPOS DE LAS VARIABLES
# dtypes() nos da los tipos Pandas de todas las variables

print(df.dtypes)

# TIPOS DE UNA VARIABLE
# dtype nos da el tipo Pandas de una variable

print(df.Country.dtype)

# VISIÓN GLOBAL DE ESTADÍSTICOS

# describe()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

# Parámetros más importantes:

# - include: los tipos de datos a incluir: 'all' para todos los tipos, o un lista para tipos concretos

# la T es la traspuesta
print(df.describe().T) # por defecto solo incluye los numéricos
print(df.describe(include = "all")) # para incluirlos todos (no tiene mucho sentido )
print(df.describe(include = ["O"]).T) # o solo incluye los objetos

# IDENTIFICACIÓN DE NULOS

print(df.isna()) # array de 0 (False) y 1 (True)

# CONTEO DE NULOS POR VARIABLES

print(df.isna().sum().sort_values(ascending = False))

# PORCENTAJE DE NULOS POR VARIABLES

print(df.isna().mean().sort_values(ascending = False) * 100) # en variasbles 0 y 1 la media es equivalente a la proporción 

# IDENTIFICACIÓN DE DUPLICADOS

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html 

print(df.duplicated().sum())

# LOCALIZAR LOS DUPLICADOS

# Usando duplicated() para filtrar como booleano.

# Parámetros más importantes:

# - subset: lista con los campos concretos que queremos usar para ver si hay duplicados
# - keep: qué registro marca como el duplicado: el primero ('first'), el último ('last') o todos (False)

# Podemos hacer la indexación de un datafrane por boolean
print(df[df.duplicated()])
print(df[df.duplicated(keep = False)])
print(df[df.duplicated(subset = "Funded Amount")])

# NÚMERO DE VALORES ÚNICOS

# nunique()

# https://pandas.pydata.org/docs/reference/api/pandas.Series.nunique.html

# Parámetros más importantes:

# - dropna: poner a False si queremos que cuente también los nulos

print(df.nunique()) # si una variable tiene todos los valores iguales es una constante o categóricas con muchos valores (p.e. como el código postal)

# Para una variable en concreto:

print(df.Country.nunique()) # saber cuantos valores únicos hay
print(df.Country.unique()) # para ver los valores únicos de esa variable

# ESTADÍSTICOS BÁSICOS
# Diferentes funciones para comprobar básicos como medias, máximos, etc.
# Podemos hacerlo sobre todo el dataset, sobre una variable o con un método select_dtype() para coger un tipo de variable concreto

# PARA VARIABLES CATEGÓRICAS

# CONTEO DE FRECUENCIAS

# value_counts()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html

# Parámetros más importantes:

# - normalize: si lo ponemos a True devuelve tantos por uno
# - sort: por defecto ordena por frecuencia en descendente

print(df.Country.value_counts())
print(df.Country.value_counts(normalize = True) * 100)

# MODA
print(df.Country.mode())

# PARA VARIABLES CONTÍNUAS

# MEDIA
print(df["Paid Amount"].mean())

# MEDIANA
print(df["Paid Amount"].median())

# MÁXIMO
print(df["Paid Amount"].max())

# MÍNIMO
print(df["Paid Amount"].min())

# ÍNDICE DEL MÍNIMO
# Localizar el índice del valor máximo
print(df["Paid Amount"].idxmax())
print(df.loc[1722])

# ÍNDICE DEL MÁXIMO
# Localizar el índice del valor mínimo
print(df["Paid Amount"].idxmin())
print(df.loc[1950])

# CORRELACIÓN

# corr()

# Podemos hacer varios tipos de correlación con el parámetro method.

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

# Parámetros más importantes:

# - method: pearson, kendall, spearman

# CORRELACIÓN PARA VARIABLES CONTÍNUAS
# Se suele utilizar Pearson (cuando son variables contínuas y tienen una distribución normal)
df_number = df.select_dtypes(["number"])
print(df_number.corr()) # medimos si existe una relación lineal

# Si solo queremos la correlación entre 2 variables tenemos que usar la sintaxis de Series:
print(df["Funded Amount"].corr(df["Loan Amount"]))

# CORRELACIÓN PARA VARIABLES ORDINALES
# Si las variables no son continuas y si ordinales. O si son contínuas pero no se distribuyen normalmente. 
# Se usa Tau de Kendall o Rho de Spearman. Detectan si existe relación monotónica entre variables
print(df["Funded Amount"].corr(df["Loan Amount"], method = "kendall"))

# SELECCIONAR VARIABLES POR SU TIPOLOGÍA

# select_dtypes()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html

# Nos permite filtrar el dataset solo para el tipo de variable que queremos y aplicar los métodos de análisis que correspondan a ese tipo.

print(df.select_dtypes("number").mean())
print(df.select_dtypes("object").mode())
print(df.select_dtypes("object").mode().T)

# To select aprint(df.select_dtypes("object").mode())ll numeric types, use np.number or 'number'
# To select strings you must use the object dtype, but note that this will return all object dtype columns
# To select datetimes, use np.datetime64, 'datetime' or 'datetime64'
# To select timedeltas, use np.timedelta64, 'timedelta' or 'timedelta64'
# To select Pandas categorical dtypes, use 'category'
# To select Pandas datetimetz dtypes, use 'datetimetz' (new in 0.20.0) or 'datetime64[ns, tz]'

# EXTRA

# Calidad de datos automática con pandas profiling y funpymodeling

# PANDAS-PROFILING

# https://github.com/pandas-profiling/pandas-profiling

# conda install -c conda-forge pandas-profiling

from ydata_profiling import ProfileReport

informe = ProfileReport(df)
informe.to_file("informe.html")

# FUNPYMODELING

# pip install funpymodeling
# import funpymodeling as fp
# fp.status(df)

