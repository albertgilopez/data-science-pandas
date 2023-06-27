print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("*********************************")
print("ESTRUCTURAS DE DATOS - EJERCICIOS")
print("*********************************")

import numpy as np
import pandas as pd
import seaborn as sns

# Documentación de Pandas https://pandas.pydata.org/pandas-docs/stable/reference/index.html

df = sns.load_dataset('tips')
print(df.head())

print("***********")
print("EJERCICIO 1")
print("***********")

# Comprueba cuantas filas va a mostrar este notebook por defecto.

print(pd.options.display.min_rows) # por defecto muestra 10 (5 superiores y 5 inferiore)

print("***********")
print("EJERCICIO 2")
print("***********")

# Cambialo para que solo muestre 6 por defecto. Y después saca df por consola para comprobarlo.

pd.options.display.min_rows = 6
print(pd.options.display.min_rows) # por defecto muestra 10 (5 superiores y 5 inferiore)

print(df)

print("***********")
print("EJERCICIO 3")
print("***********")

# Crea una Series a partir de una lista, un diccionario y un array.

lista = [1,2,3] # para crear una serie a partir de una lista de NumPy
serie_lista = pd.Series(lista)
print(serie_lista)
print(type(serie_lista))

array = np.array([1,2,3]) # para crear una serie a partir de un array de NumPy
serie_array = pd.Series(array)
print(serie_array)
print(type(serie_array))

diccionario = {"A":1,"B":2,"C":3} # para crear una serie a partir de un diccionario
serie_diccionario = pd.Series(diccionario)
print(serie_diccionario) 
print(type(serie_diccionario))

print("***********")
print("EJERCICIO 4")
print("***********")

# Crea un DataFrame a partir de una lista, un diccionario y un array.

lista = [["Albert",29,True],["Angels",24,True],["Reina",1,True]] # un dataframe a partir de un lista
df_lista = pd.DataFrame(lista, columns = ["Nombre","Edad","Felicidad"])
print(df_lista)
print(type(df_lista))

vector = np.array([[1,2,3],["A","B","C"]]) # un dataframe a partir de un array
df_array = pd.DataFrame(vector)
print(df_array)
print(type(df_array))

diccionario = {"Letras":["A","B","C"], "Numeros":[1,2,3]} # un dataframe a partir de un diccionario
df_diccionario = pd.DataFrame(diccionario)
print(df_diccionario)
print(type(df_diccionario))

print("***********")
print("EJERCICIO 5")
print("***********")

# Extrae la columna tip de nuestro df como una Serie, guárdala en un objeto llamado tip y sácala por consola.

print(df)

tip = pd.Series(df["tip"]) # o df.tip
print(tip)

print("***********")
print("EJERCICIO 6")
print("***********")

# Comprueba el tipo de tip.

print(type(tip))

print("***********")
print("EJERCICIO 7")
print("***********")

# Transforma tip a un array de numpy, guárdalo en un objeto llamado vector y saca por pantalla solo los 10 primeros valores.

vector = tip.to_numpy()
print(vector[0:10]) # vector[:10]
print(type(vector))

print("***********")
print("EJERCICIO 8")
print("***********")

# Transforma tip a un DataFrame y sácalo por pantalla.

tip_df = tip.to_frame()
print(tip_df)
print(type(tip_df))

print("***********")
print("EJERCICIO 9")
print("***********")

# Ahora extrae la columna tip de nuestro df como un DataFrame, guárdala en un objeto llamado tip_df y sácalo por consola.

tip_df = pd.DataFrame(df["tip"])
print(tip_df)
print(type(tip_df))

print("************")
print("EJERCICIO 10")
print("************")

# Transforma tip_df a una Serie

print(type(tip_df["tip"])) # extraer con corchetes y devuelve un Series
print(tip_df["tip"])

