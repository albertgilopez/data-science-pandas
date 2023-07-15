print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("**************************************")
print("CALIDAD DE DATOS - UNIÓN E INTEGRACIÓN")
print("**************************************")

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

# Es muy común que en un proyecto real no partamos de una fuente de datos ya unificada, si no que tengamos varios ficheros origen que tengamos que unir.
# Por ejemplo podríamos tener una tabla de ventas por un sitio, otra con los datos de los clientes y otra con los datos de los productos.
# O la información de sociodemográficos en un fichero y de la transaccionalidad en otro, etc.

# Lo principal es saber los diferentes tipos de "unión" de ficheros que podemos hacer. Hay 2 grandes formas de hacerlo:

# - Si NO existe una variable clave compartida entre los 2 ficheros
# - Si SI existe una variable clave compartida entre los 2 ficheros

# En el primer caso hablamos de "apilar", y puede ser tanto apilar variables como apilar registros.
# En el segudo caso hablamos de "cruzar", y existen varios tipos de cruce, los más importantes son left join, right join, inner join y full join.

# Para poder hacer los ejemplos de esta parte necesitamos crear nuevos ficheros a partir de nuestro df, simplemente a modo de fake data:

# Para los ejemplos de apilar:

# - variables_izq: con la mitad izquierda de las variables y sin identificador
# - variables_drc: con la mitad derecha de las variables y sin identificador
# - registros_sup: con la mitad superior de los registros y sin identificador
# - registros_inf: con la mitad inferior de los registros y sin identificador

# Para los ejemplos de cruzar:

# - fichero1: con la mitad izquierda de las variables y CON identificador
# - fichero2: con la mitad derecha de las variables y CON identificado

# Creamos los de apilar

variables_izq = df.iloc[:,:6]
variables_drc = df.iloc[:,6:]

registros_sup = df.iloc[:2573,:]
registros_inf = df.iloc[2573:,:]

# Creamos los de cruzar
# Primero tenemos que crear un campo clave

df2 = df.copy()
df2.insert(0,'Clave',np.arange(0,len(df))) # Creamos un identificador "Clave" del tamañao del df

# Creamos los ficheros
fichero1 = df2.copy().drop(df2.columns[8:],axis = 1)
fichero2 = df2.copy().drop(df2.columns[1:8],axis = 1) # des de la 1 porque hemos creado la "Clave"

# APILAR VARIABLES

# Apilar variables significa que tenemos dos ficheros que tienen los mismos registros, pero diferentes columnas que se complementan y queremos unir
# Pero NO tenemos un campo clave, así que es imprescindible que tengan EXACTAMENTE los mismos registros y en EL MISMO ORDEN.

# Lo hacemos con concat(), espeficiando axis = 'columns'

# - objs: los ficheros a unir pasados como una lista
# - axis: 'columns' para apilar variables

print(variables_izq)
print(variables_drc)

pd.concat([variables_izq,variables_drc], axis = 'columns') # apilamos variabes

# APILAR REGISTROS

# Apilar registros significa que tenemos dos ficheros que tienen las mismas variables, pero diferentes registros que se complementan y queremos unir.
# Pero NO tenemos un campo clave, así que es imprescindible que tengan EXACTAMENTE las mismas variables y CON EL MISMO NOMBRE.

# Lo hacemos con concat(), espeficiando axis = 'index'

# - objs: los ficheros a unir pasados como una lista
# - axis: 'index' para apilar registros

print(registros_sup)
print(registros_inf)

pd.concat([registros_sup,registros_inf], axis = 'index') # apilamos registros

# CRUZAR FICHEROS POR CAMPO CLAVE

# Esta suele ser la operación más habitual en entornos profesionales ya que los ficheros muchas veces vienen de tablas de bbdd y éstas suelen tener campos clave.

# Se hace con merge(): https://pandas.pydata.org/docs/reference/api/pandas.merge.html

# Podemos hacer diferentes tipos de cruce según la tabla que queremos que "mande":

# - left join: manda la izquierda, es decir se incluirán todos los registros de la tabla de la izquierda independientemente de que estén o no en la derecha
# - rigth join: manda la derecha, es decir se incluirán todos los registros de la tabla de la derecha independientemente de que estén o no en la izquierda
# - inner join: solamente se incluirán los registros que estén en ambas tablas
# - full join: se incluirán todos los registros tanto los de la izquierda como los de la derecha

# Parámetros más importantes:

# - left: la tabla de la izquierda
# - right: la tabla de la derecha
# - how: 'left', 'right', 'inner', 'outer' según lo comentado anteriormente
# - on: el nombre del campo clave para unir (si se llama igual en ambas)
# - left_on: el nombre del campo clave en la izquierda
# - right_on: el nombre del campo clave en la derecha

print(fichero1)
print(fichero2)

# Cruzamos, en este caso tienen exactamente los mismos registros, así que daría igual el tipo de unión

pd.merge(left = fichero1,
         right = fichero2,
         how = 'inner',
         on = 'Clave')

# También se podría hacer sobre uno de los 2 ficheros, usando merge como método de Series para añadir el segundo

fichero1.merge(right = fichero2,
         how = 'left',
         on = 'Clave')