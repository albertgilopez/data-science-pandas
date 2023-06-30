print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("***********************")
print("INDEXACIÓN - EJERCICIOS")
print("***********************")

import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('tips')
print(df.head())

print("***********")
print("EJERCICIO 1")
print("***********")

# Extrae la variable smoker por nombre

print(df.loc[:,"smoker"])

print("***********")
print("EJERCICIO 2")
print("***********")

# Extrae la variable smoker por posición

print(df.iloc[:,3])

print("***********")
print("EJERCICIO 3")
print("***********")

# Extrae las variables sex y time por nombre

print(df.loc[:,["sex","time"]])

print("***********")
print("EJERCICIO 4")
print("***********")

# Extrae las variables sex y time por posición

# Si existen muchas variables, una manera de saber la posición es utilizar el método:

print(df.info())

print(df.iloc[:,[2,5]])

print("***********")
print("EJERCICIO 5")
print("***********")

# Extrae las variables sex hasta time por nombre

print(df.loc[:,"sex":"time"])

print("***********")
print("EJERCICIO 6")
print("***********")

# Extrae las variables sex hasta time por posición

print(df.iloc[:,2:6])

print("***********")
print("EJERCICIO 7")
print("***********")

# Extrae todas las variables que empiecen por s.

print(df.loc[:,df.columns.str.startswith("s")])

print("***********")
print("EJERCICIO 8")
print("***********")

# Extrae todas las variables que empiecen por s y además la variable total_bill.

criterio = (df.columns.str.contains("total_bill")) | (df.columns.str.startswith("s")) # df.columns == "total_bill"
print(df.loc[:,criterio])

print("***********")
print("EJERCICIO 9")
print("***********")

# Extrae todas las variables cuyo nombre tenga más de 5 letras y además la variable tip.

criterio = (df.columns.str.len() > 5) | (df.columns.str.contains("tip")) # df.columns == "tip"
print(df.loc[:,criterio])

print("************")
print("EJERCICIO 10")
print("************")

# Pon la variable day como el index y muestra df por consola.

df.set_index("day", inplace = True)
print(df)

print("************")
print("EJERCICIO 11")
print("************")

# Selecciona solo los registros de los jueves (Thur).

print(df.loc["Thur"])

print("************")
print("EJERCICIO 12")
print("************")

# Selecciona solo los registros de los jueves y de los sábados(Thur, Sat).

print(df.loc[["Thur","Sat"]])

print("************")
print("EJERCICIO 13")
print("************")

# Elimina el índice para que vuelva a ser el automático y saca df por consola.

df.reset_index(inplace = True) # para resetear la variable asignada al índice
print(df)

print("************")
print("EJERCICIO 14")
print("************")

# Extrae el segundo registro.

# Para obtener la posición de un elemento determinando del índice

print(df.iloc[1])
# print(df.loc[1]) # esto nos lo muestra correcto porque justamente el nombre 1 es la misma posición que queremos recuperar

print("************")
print("EJERCICIO 15")
print("************")

# Extrae los registros desde el segundo hasta el décimo. 

print(df.loc[1:9]) # por rango

print("************")
print("EJERCICIO 16")
print("************")

# Extrae solo los registros de hombres

print(df[(df.sex == "Male")]) # siempre entre ()

print("************")
print("EJERCICIO 17")
print("************")

# Extrae solo los registros de hombres que además sean fumadores.

print(df[(df.sex == "Male") & (df.smoker == "Yes")]) # siempre entre ()

print("************")
print("EJERCICIO 18")
print("************")

# Extrae solo los registros de mujeres que hayan dejado una propina superior a 5$.

print(df.loc[(df.sex == "Female") & (df["tip"] > 5)]) # No tengo que indicar el índice porque solo estoy indexando por columnas

print("************")
print("EJERCICIO 19")
print("************")

# Extrae solo la variable tip de los registros entre el 10 y el 20.

print(df.loc[9:20,"tip"])

print("************")
print("EJERCICIO 20")
print("************")

# Extrae solo la variables total_bill y tip de los registros entre el 10 y el 20.

print(df.loc[9:20,["tip","total_bill"]])

print("************")
print("EJERCICIO 21")
print("************")

# Extrae solo la variables entre total_bill y smoker de los registros entre el 10 y el 20.

print(df.loc[9:20,"total_bill":"smoker"])

print("************")
print("EJERCICIO 22")
print("************")

# Extrae los registros con total_bill mayor de 30 y solo las variables que tengan una t en su nombre.

print(df.loc[(df["total_bill"] > 30), (df.columns.str.contains("t"))]) # siempre entre ()

print("************")
print("EJERCICIO 23")
print("************")

# Extrae los registros con total_bill mayor de 30 o con propinas menos que 2, además solo las variables que tengan una t en su nombre o aquellas que terminen en r

criterio_filas = (df["total_bill"] > 30) | (df["tip"] < 2)
criterio_columnas = (df.columns.str.contains("t")) | (df.columns.str.endswith("r"))
print(df.loc[criterio_filas,criterio_columnas])

print("************")
print("EJERCICIO 24")
print("************")

# Selecciona por posición el dato del primer registro y la variable day

print(df.head())
print(df.iloc[0,0]) # print(df.columns.get_loc("day"))

print("************")
print("EJERCICIO 25")
print("************")

# Selecciona por posición el dato de los registros tercero y sexto, y las variables total_bill y tip

print(df.iloc[[2,5],[1,2]]) # una fila y una columna

print("************")
print("EJERCICIO 26")
print("************")

# Selecciona por posición el dato de los registros del tercer al quinto y las variables de total_bill a smoker

print(df.iloc[2:5,1:4]) # una fila y una columna
