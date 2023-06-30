print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("**********")
print("INDEXACIÓN")
print("**********")

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

# CÓMO INDEXAR UN DATAFRAME

# Es algo complejo porque existen varios escenarios para hacerlo:

# - Cómo indexar por columnas.
# - Cómo indexar por filas.
# - Cómo indexar ambas.

# Además, dentro de cada un podemos:

# - Indexar por nombre.
# - Indexar por posición.
# - Indexar por criterio, es decir, que cumpla unas condiciones.

# Y además, tres modalidades:

# - Indexación simple: un sólo elemento.
# - Indexación múltiple: varios elementos a la vez especificados de forma explícita.
# - Indexación por rango: varios elementos a la vez especificados mediante un rango.

# Si los datos y traen un índice válido, como en el dataset de ejemplo, cuando hagamos la importación se lo podemos indicar

df = pd.read_csv(datos, sep = ";", index_col = "id")
print(df.head(3))

# Hay ciertos métodos en Pandas (que implican cambios en el dataset) en los que hay que confirmar las modificaciones, para ello usamos inplace = True
df.reset_index(inplace = True) # para resetear la variable asignada al índice
print(df.head(3))

# Si quisiéramos poner un índice después de haber hecho la importación
df.set_index("id", inplace = True)
print(df.head(3))

# Para obtener la posición de un elemento determinando del índice
print(df.index.get_loc(85))

# CAMBIAR UN ELEMENTO DEL ÍNDICE

# df.rename(index = {"valor_viejo":"valor_nuevo"}, inplace = True)
df.rename(index = {85:185}, inplace = True)
print(df.head(3))

# Podemos cambiar varios a la vez, simplemente deberíamos incluir más elementos al diccionario

# df.rename(columns = {"valor_viejo":"valor_nuevo"}, inplace = True)
df.rename(columns = {"Status":"Estado"}, inplace = True)
print(df.head(3))

# Podemos cambiar varios a la vez, simplemente deberíamos incluir más elementos al diccionario

df.reset_index(inplace = True) # para usar el índice automático
print(df.head(3))

# MULTI-INDICES
# Un dataframe puede tener más de un índice. Útil para tareas de hacer queries, por ejemplo, cliente-producto

diccionario = {"Cliente": ["A","A","B","B","B","C","C"],
			   "Producto": ["1","2","1","2","3","2","3"],
			   "Importe": ["100","200","100","200","300","200","300"]}

tabla_mi = pd.DataFrame(diccionario)
print(tabla_mi)

tabla_mi.set_index(["Cliente","Producto"],inplace = True) # establecemos un multi-indice
print(tabla_mi) # visualmente también nos ayuda a entenderlo

print(tabla_mi.loc["B"])
print(tabla_mi.loc[("B","2")]) # hay que pasar el parámetro como una tupla

print(tabla_mi.xs("B"))
print(tabla_mi.xs("3", level = "Producto")) # método (cross-section) para acceder al índice secundario
print(tabla_mi.xs(("B","2")))

# También podemos mover los multi-indices a columns, es decir, un multi-columns.

print(tabla_mi)

tabla_mc = tabla_mi.unstack() # por defecto, el índice secundario

print(tabla_mc) # hay que tener en cuenta que, al hacer estas combinacione se pueden generar nulos, como en este caso
print(type(tabla_mc)) # sigue siendo un objetio DataFrame

# Una aplicación es en la fase de calidad de datos, cuando aplicamos diferentes estadísticos por variable

# Para rellenar los nulos utilizamos el siguiente método (rellenar con el dato que queramos)
# print(tabla_mc.unstack(fill_value = 0))

# También podemos convertir el índice principal en multi-column
# En este caso funciona por niveles, el primero es -1, -2, -3...
# tabla_mc = tabla_mi.unstack(level = -2) # convertimos en multi-column el índice "Cliente"
# print(tabla_mc)

# El método inverso se hace con el siguiente método:

tabla_mc = tabla_mc.stack()
print(tabla_mc)

# También podemos eliminar niveles de índice para tener vistas concretas
# Este caso también funciona por niveles, el primero es -1, -2, -3...

# tabla_mc = tabla_mc.stack().droplevel(-2)
# print(tabla_mc)

# O haciendo un reset y eliminado los multi-indices

tabla_mc.reset_index(inplace = True)
print(tabla_mc)

# CÓMO INDEXAR COLUMNAS

df = pd.read_csv("../../../00_DATASETS/DataSetKivaCreditScoring.csv", sep = ";") # Datos para los ejemplos
print(df.head(2))

# POR NOMBRE

print(df.Country) # no sirve cuando el nombre de la variable tenga espacios, ni para indexar varias variables a la vez, ni para crear variables nuevas

print(df["Country"])
print(df[["Country"]]) # con dos [[]] nos devuelve un dataframe
print(df[["Country","Country Code"]]) # para indexar varias variables se le pasa una lista

# df["País"] = df.Country # para crear nuevas variables o renombrar

# .loc es la manera recomendada por la documentación
# Si solo le pasamos un parámetro indexará las filas
# Si indicamos : significa que queremos recuperar todos los valores

print(df.loc[:,"Country"])
print(df.loc[:,["Country","Country Code"]])
print(df.loc[:,"Country":"Sector"]) # columnas entre Country y Sector

# POR POSICIÓN

print(df.iloc[:,0]) # una columna
print(df.iloc[:,[2,5]]) # dos columnas específicas
print(df.iloc[:,2:5]) # un rango de columnas entre 2 y 5

# POR CRITERIO (prefijos, sufijo, que contengan un texto concreto, etc.)

print(df.columns) # para saber que columnas hay

# Con el str tenemos diferentes métodos (contains, upper, split...)

print(df.loc[:,df.columns.str.contains("Amount")]) # una columna
print(df.loc[:,df.columns.str.contains("Amount") | df.columns.str.startswith("Paid")]) # varios criterios específicos

# O primero extraer el criterio

criterio = df.columns.str.contains("Amount") | df.columns.str.startswith("Paid")
print(criterio)

print(df.loc[:,criterio])

# CÓMO INDEXAR FILAS

# POR NOMBRE

print(df.loc[0]) # como solo le pasamos un valor entiende que es el índice (pero 0 es el nombre, no es la posición)
print(df.loc[[0,5]]) # filas específicas
print(df.loc[0:5]) # por rango

# Para entenderlo, por ejemplos vamos a indexar por Country

df.set_index("Country", inplace = True) # no tiene porque ser un indentificar único
print(df)

print(df.loc["Uganda"]) # queremos sacar todos los registros de Uganda
print(df.loc[["Uganda", "Ghana"]])

# POR POSICIÓN

df.reset_index(inplace = True) # reseteamos el índice para seguir con los ejemplos

print(df.iloc[0]) # por posición, aquí el 0 si que se corresponde con la posición o el nombre 0
print(df.iloc[[0,5]]) # posiciones específicas
print(df.iloc[0:5]) # por rango

# POR CRITERIO

# Utilizando []
print(df[df["Funded Amount"] > 1000]) # un criterio, lo aplicamos con corchetes (devuelve un vector lógico)
# o sacanado el criterio fuera criterio = df["Funded Amount"] > 1000]

# Utilizando .loc
print(df.loc[df["Funded Amount"] > 1000]) # 

# Utilizando un criterio, entre []
print(df[(df["Funded Amount"] > 1000) & (df.Activity == "Restaurant")]) # siempre entre ()
# o sacanado el criterio fuera criterio = (df["Funded Amount"] > 1000) & (df.Activity == "Restaurant")

# CÓMO INDEXAR FILAS Y COLUMNAS
# Para indexar a la vez filas y columnas usaremos siempre loc o iloc, sin corchetes ni puntos

# POR NOMBRE

print(df.loc[0,"Country"]) # una fila y una columna
print(df.loc[[0,5],["Country","Country Code"]]) # filas y columnas específicas
print(df.loc[0:5,"Country":"Country Code"]) # filas y columnas por rango concreto

# POR POSICIÓN

print(df.iloc[0,0]) # una fila y una columna
print(df.iloc[[0,5],[3,6]]) # varias filas y columnas específicas
print(df.iloc[0:5,3:6]) # por rango

# POR CRITERIO

print(df.loc[df["Funded Amount"] > 1000, df.columns.str.startswith("Funded")]) # un criterio en la fila y otro en la columna

# Varios criterios tanto en las filas como en las columnas
# Sacamos los criterios fuera simplemente por legibilidad

criterio_filas = (df["Funded Amount"] > 1000) & (df.Sector == "Food")
criterio_columnas = (df.columns.str.startswith("Funded")) | (df.columns.str.contains("Date"))
print(df.loc[criterio_filas,criterio_columnas])
