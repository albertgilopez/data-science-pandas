print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("********************")
print("ESTRUCTURAS DE DATOS")
print("********************")

import pandas as pd
import numpy as np 

# Documentación de Pandas https://pandas.pydata.org/pandas-docs/stable/reference/index.html

datos = "../../../00_DATASETS/DataSetKivaCreditScoring.csv" # Datos para los ejemplos

print(pd.options.display.min_rows) # por defecto muestra 10 (5 superiores y 5 inferiore)
print(pd.read_csv(datos, sep = ";"))

pd.options.display.min_rows = 6
print(pd.read_csv(datos, sep = ";")) # ahora nos muestra 6

# Extraemos "Funded Amount" como Series (columnas)
df = pd.read_csv(datos, sep = ";")
print(df["Funded Amount"])

# Axis 0 / Index. Etiquetas del índice 0, 1, 2 ... 5143, 5144, 5145
# Axis 1 / Columns. Nombre de las variables: Funded Amount, ID...
# Valores. 500, 500, 500 ... 1000, 1100, 800
# Nombre de la serie. Funded Amount
# Num de elementos. Length: 5146
# Tipo de datos: dtype: int64
# Datos truncados ...

# TIPOS DE DATOS

# En Pandas, el index, columns y los propios dato son arrays multidimensionales en Numpy
# Luego, Pandas tiene tipo de datos propios, como category o Int64.

# float: es el float de Numpy, que soporta datos nulos
# int: es el int de Numpy, que NO soporta datos nulos

# Int64: es un int que introduce Pandas para soportar datos nulos -> Desde las nuevas versiones, para solucionar el siguiente ejemplo

# object: es el object de Numpy, que se usa como texto para meter cualquier cosa
# Por ejemplo, si tenemos una tabla con la edad (int) y tenemos algún dato faltante, Pandas lo convertirá todo en object

# category: es un tipo que introduce Pandas específicamente para variables categóricas (sexo, clase social, etc.)
# bool: es el booleano de Numpy, que NO soporta datos nulos
# boolean: es el booleano que introduce Pandas para soportar datos nulos
# datetime64: es el tipo de Numpy para las fechas, que NO soporta datos nulos

# Por defecto, Pandas importa los datos como un dato de 64 bits, aunque por lo general necesitará mucho menos espacio para almacenarlo
# Cuando trabajamos con muchos datos, una manera de optimizar el dataset es convertir los tipos de datos:

# int8 puede almacenar enteros desde -128 hasta 127
# int16 puede almacenar enteros desde -32768 hasta 32767
# int64 puede almacenar enteros desde -9223372036854775808 hasta 9223372036854775807

# Si alguna variable tiene nulos, este dato lo importará como object, como decíamos

print(df.info()) # podríamos cambiar algún object por category y transformar los int

# CREAR DATOS

serie = pd.Series(["A","B","C"])
print(serie)

print(serie.index) # para acceder a los índices
print(serie.values) # para acceder a los valores, como un elemento de NumPy (array)

indice = ["10","20","30"]
valores = ["A","B","C"]
serie = pd.Series(valores, index = indice) # para crear un serie con un índice personalizado (tiene que tener la misma longitud)
print(serie)

diccionario = {"A":1,"B":2,"C":3} # para crear una serie a partir de un diccionario, en este caso el índice serán las claves del diccionario

serie = pd.Series(diccionario)
print(serie) 

vector = np.array([1,2,3]) # para crear una serie a partir de un array de NumPy
serie = pd.Series(vector)
print(serie) 

# para hacerlo al revés, de array de NumPy a Series hay dos maneras:

# .values: funciona pero no es recomendable
# to_numpy()

print(type(serie.values))
print(type(serie.to_numpy()))

print(serie)
df = serie.to_frame() # para pasar una serie a un dataframe
print(df)

# INDEXANDO UNA SERIE

# Por posición: pasándole la posición en el índice del elemento que queremos
# Por nombre: pasándole el nombre del índice del elemento que queremos

serie = pd.Series(diccionario)

print(serie[0])
print(serie['A'])

# Las Series tienen diferentes atributos, por ejemplo:

print(serie.dtype)
print(serie.size)

# Lista de atributos y métodos de una Serie: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html

# DATAFRAMES

# Lista de atributos y métodos de un DataFrame: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

# En esta estructura, cada clave del diccionario será una columna y cada valor será una lista con todas las futuras filas de esa columna

diccionario = {"Letras":["A","B","C"], "Numeros":[1,2,3]} # la clave será la columna y los elementos serán los valores
df_diccionario = pd.DataFrame(diccionario)
print(df_diccionario)

# También se puede personalizar el índice, por ejemplo:

diccionario = {"Letras":["A","B","C"], "Numeros":[1,2,3]} # la clave será la columna y los elementos serán los valores
df_diccionario = pd.DataFrame(diccionario, index = [10,20,30])
print(df_diccionario)

# Un dataframe, en definitiva, necesita datos, nombres de columnas y un índice
# En el caso de los datos, hay que pasar la información como fila, no como columnas

datos = [["A",1],["B",2],["C",3]] # una lista de listas con el orden correcto, en el ejemplo: A sería un cliente con el valor 1, etc.
columnas = ["Letras","Números"]
indice = [10,20,30]

df_diccionario = pd.DataFrame(data = datos, columns = columnas, index = indice)
print(df_diccionario)

vector2D = np.array([[1,2,3],["A","B","C"]]) # un dataframe a partir de un array (solo incluye los valores)
df_2D = pd.DataFrame(vector2D)
print(df_2D)

# El resto de datos se lo podemos introducir manualmente, como por ejemplo:

vector2D = np.array([[1,2,3],["A","B","C"]]) # un dataframe a partir de un array (solo incluye los valores)
df_2D = pd.DataFrame(vector2D, index = ["Fila1", "Fila2"], columns = ["Columna1", "Columna2", "Columna3"])
print(df_2D)

# Y volve a pasar de dataframe a array de dos maneras:

# .values: funciona pero no es recomendable
# to_numpy()

print(type(df_2D.values))
print(type(df_2D.to_numpy()))

# Finalmente, vamos a pasar de dataframes a series
# Un dataframe es una colección de Series, y existen vario método para extraerlas:

vector2D = np.array([[1,2,3],["A","B","C"]])
df_2D = pd.DataFrame(vector2D, index = ["Fila 1", "Fila 2"], columns = ["Columna1", "Columna2", "Columna3"])

print(type(df_2D.Columna1)) # extraer con . y devuelve un Series
print(df_2D.Columna1)

print(type(df_2D["Columna1"])) # extraer con corchetes y devuelve un Series
print(df_2D["Columna1"])

print(type(df_2D[["Columna1"]])) # extraer con doble corchete y devuelve un DataFrame
print(df_2D[["Columna1"]])
