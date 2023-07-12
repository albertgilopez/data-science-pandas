print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("*****************************")
print("CALIDAD DE DATOS - CORRECCIÓN")
print("*****************************")

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

# CONVERTIR TIPOS DE VARIABLE

# Tenemos dos formas para convertir tipos de variables:

# - Con el método general astype() y especificando el tipo deseado
# - Con métodos concretos para ciertos tipos de datos

# CONVERTIR TIPOS CON ASTYPE()

# astype()

# Convierte al tipo especificado. Notar que no convierte inplace (es decir, solo nos visualiza, para confirmar el cambio hay que asignar la variable)

# https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html

# Ejemplos de tipos los que podemos convertir: int, float, category, object, etc.

print(df.dtypes)

# Convertimos country a categórica

print(df.Country.astype('category').dtype)

# Para que Country guarde el cambio de tipo hay que asignar la variable
# df["Country"] = df.Country.astype('category')

tipos = {'Funded Amount':'float',
         'Country Code':'category',
         'Delinquent':'int'}

print(df.astype(tipos).dtypes)

# O convertir por bloques combinándola con select_dtypes()
print(df.select_dtypes('object').astype('category').dtypes)

# CONVERTIR TIPOS CON FUNCIONES CONCRETAS

# CONVERTIR A TIPO NUMÉRICO

# to_numeric()

# https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html

# Parámetros más importantes:

# - errors: personaliza el comportamiento cuando no pueda convertir algo. Lo más típico es ponerlo a 'coerce' que forzará un nulo

print(pd.to_numeric(df['Funded Date']).dtype)

# CONVERTIR A TIPO FECHA

# to_datetime()

# https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

# Parámetros más importantes:

# - errors: personaliza el comportamiento cuando no pueda convertir algo. Lo más típico es ponerlo a 'coerce' que forzará un nulo
# - infer_datetime_format: si True intenta inferir automáticamente el formato
# - format: el formato de la cadena que le estamos pasando. Para los códigos ver: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# En muchos casos por defecto lo hará bien automáticamente
print(pd.to_datetime('13/08/2020'))

# En muchos casos por defecto lo hará bien automáticamente
print(pd.to_datetime('13-Aug-2020'))

# Pero a veces no lo hace bien
# print(pd.to_datetime('13082020'))

#Y podemos corregirlo con el format
print(pd.to_datetime('13082020', format='%d%m%Y'))

# Ahora, para cambiar el formato de una fecha, podemos cambiar su formato con .dt.strftime()
# Los códigos de formato son los mismos: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# Así es el formato origen de nuestra fecha
print(df['Funded Date'].head())

# Se lo cambiamos a un formato europeo
print(df['Funded Date'].dt.strftime('%d/%m/%Y'))

# CONVERTIR A UN TIPO CATEGÓRICA ORDENADA

# Las variables categóricas normalmente serán nominales, es decir sin tener un orden.
# Pero también es muy frecuente que tengan un orden, siendo entonces ordinales.

# Si Pandas ha importado la variable como object es buena práctica pasarla a categórica, entre otras cosas será mucho más eficiente en tamaño y procesamiento.

# - Para convertir a nominal podemos usar el astype('category') que ya conocemos.
# - Para convertir a ordinal y establecer el orden de una variable usamos CategoricalDtype().

# El proceso a seguir es:

# - Crear el orden deseado pasándole una lista y el parámetro ordered = True a CategoricalDtype()
# - Pasarle ese orden a astype() como una conversión normal

# https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html

# Por ejemplo vamos a convertir Status a una categórica ordenada

# Primero comprobamos el tipo actual
print(df.Status.dtype)

# Comprobamos los diferentes valores que puede tomar
print(df.Status.unique())

# Definimos el orden
orden_Status = pd.CategoricalDtype(['deleted','defaulted','paid','refunded'], ordered = True)

# Aplicamos el orden y comprobamos sus valores
df['Status'] = df['Status'].astype(orden_Status)
print(df['Status'].unique())

# Y vemos que ahora ya su tipo es categórico ordenado
print(df['Status'].dtype)

# Ahora, si la variable ya fuera categórica, pero sin orden, o incluso si ya tiene orden pero queremos cambiarlo. Entonces usaremos .cat.set_categories().

# Por ejemplo vamos a cambiar el orden poniendo 'paid' primero.

df["Status"] = df.Status.cat.set_categories(['paid','deleted','defaulted','refunded'], ordered = True)

print(df.Status)

# ELIMINAR VARIABLES O REGISTROS

# drop()

# Elimina variables o registros. Notar que por defecto no es inplace. Drop elimina por nombre, no por posición.
# Si quisiéramos eliminar por posición deberíamos obtener primero los nombres de las posiciones a eliminar con .index()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html

# Parámetros más importantes:

# - index: para eliminar registros
# - columns: para eliminar variables
# - inplace: por defecto es False

df = df.drop(columns = ['Funded Date','Funded Amount']) # eliminar variables
df = df.drop(index = [84,85]) # eliminar registros

print(df.info())
print(df.head(2))

# Para eliminar registros por posición, ej los 5 primeros, obtenemos su nombre con index

a_eliminar = df.index[0:5]
print(a_eliminar)

df = df.drop(index = a_eliminar)

print(df.info())
print(df.head(2))

# INSERTAR VARIABLES

# insert()

# Se usa cuando queremos insertar una nueva variable en una posición determinada. Notar que hace el inplace directamente.

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html

# Parámetros más importantes:

# - loc: la posición en la que insertar
# - column: nombre de la nueva variable
# - value: valores de la variable

df.insert(2,'Pendiente',df['Loan Amount'] - df['Paid Amount'])
print(df.info())

# ELIMINAR NULOS

# dropna()

# Elimina registros o columnas que tienen nulos. Notar que por defecto no hace inplace.

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html

# Parámetros más importantes:

# - axis: Si 0 o index elimina los registros con nulos. Si 1 o columns las variables.
# - how: por defecto 'any' que elimina todo el registro o columna simplemente con que haya un nulo. Se puede poner a 'all' que lo eliminará solo si está totalmente a nulos
# - subset: si queremos eliminar solo los nulos en algunas variables
# - thresh: un umbral para considerar eliminar todo el registro o columna. Ej que haya al menos 100 nulos
# - inplace: por defecto False

print(df.shape) # dimensiones del dataset original
print(df.dropna(axis = 1).shape) # dimensiones del dataset tras eliminar las columnas con nulos
print(df.dropna(axis = 0).shape) # dimensiones del dataset tras eliminar los registros con nulos

# REEMPLAZAR NULOS

# fillna()

# Reemplaza los nulos por otro valor. Notar que por defecto no hace inplace.
# Se puede reemplazar por un valor fijo como 0, o por un valor calculado al vuelo como la media, o con algún método como copiar el valor superior o inferior.

# https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html

# Parámetros más importantes:

# - value: para reemplazar por un valor fijo o calculado
# - method: 'ffill' para reemplazar por valor superior, 'bfill' para inferior
# - inplace: por defecto False

print(df.Status.value_counts(dropna=False)) # conteo de Status incluyendo nulos

moda_Status = df.Status.mode().values[0] 
print(df.Status.fillna(value = moda_Status).value_counts(dropna=False)) # conteo de Status tras imputar nulos por la moda

# CUIDADO: Si intentamos reemplazar por un nuevo valor en una variable categórica que no está entre los valores originales tenemos que hacer 2 pasos:

# - Añadir la nueva categoría con .cat.add_categories()
# - Reemplazar el valor
# - Pandas no añade la nueva categoría directamente.

# Por ejemplo, si Country fuera categórica, y supiéramos que sus nulos son de un país que no está entre sus valores actuales, pongamos España, y queremos imputar los nulos por España tendríamos que hacer así:

df["Country"] = df.Country.astype('category')
print(df["Country"].dtype)

# df.Country.cat.add_categories('España',inplace=True)
df["Country"] = df.Country.cat.add_categories('España')
print(df["Country"].unique())

df.Country.fillna(value = 'España', inplace=True)
print(df["Country"])

# ELIMINAR DUPLICADOS

# drop_duplicates()

# Elimina registros duplicados. (No tienen en cuenta el índice). Notar que por defecto no hace inplace.

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html

# Parámetros más importantes:

# - subset: para definirle las columnas que debe analizar, por defecto son todas
# - keep: el registro que quieres que deje, por defecto 'first' pero le puedes poner 'last'
# - inplace: por defecto False

# df.drop_duplicates(inplace = True)
df.drop_duplicates()

print(df)

# RENOMBRAR VARIABLES O INDICE

# rename()

# Reemplazar los nombres tanto de variables como de los elementos del índice usando un diccionario, con la forma {'viejo_nombre':'nuevo_nombre')
# Para renombrar variables lo usaremos con columns y para el índice con index

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html

# Parámetros más importantes:

# - inplace: por defecto False

df.rename(columns = {'Funded Date':'Fecha_financiacion',
          'Country':'Pais'})

print(df.head(2))

# TRUCO: Suele ser conveniente limpiar los nombres de variables de acentos, caracteres, espacios vacíos y demás. Incluso ponerlo todo en minúsculas.
# Podríamos ir haciéndolo nosotros paso a paso, pero hay un paquete que hace esto por nosotros de forma muy sencilla.
# Se llama Pyjanitor, y puedes instalarlo con conda install pyjanitor -c conda-forge
# E importar la función que usaremos con from janitor import clean_names.

print(df.columns)

from janitor import clean_names
print(clean_names(df))

# REEMPLAZAR VALORES

# replace()

# Reemplazar la presencia de un valor por otro en la variable (o en todo el dataframe). Notar que por defecto no hace inplace.

# https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html

# Parámetros más importantes:

# - to_replace: el valor viejo a reemplazar. Acepta cosas avanzadas como diccionarios o Regex
# - value: el nuevo valor
# - inplace: por defecto False

df.Country.replace('Uganda','Uga')

valores = {'Uganda':'Uga', 'Ghana':'Gha'}
df = df.replace(valores)

print(df)

# RECODIFICAR VALORES

# map()

# Recodifica unos valores por otros según un diccionario {'valor viejo':'valor nuevo'} o una función.
# Se podría hacer con replace() pero map es más flexible ya que admite funciones.
# Si se usa un diccionario todo valor que no esté en el diccionario será reemplazado por un nulo.

# No hace inplace.

# https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html

# Parámetros más importantes:

# - na_action: se puede poner a 'ignore' para que no aplique la función sobre los nulos y los deje como nulos

print(df.Status.value_counts(dropna=False)) # valores originales de status

# Ejemplo de recodificar con un diccionario

status_dict = {
    'paid':'pagado',
    'defaulted':'impagado',
    'deleted':'pagado'
}

print(df.Status.map(status_dict).value_counts(dropna=False))

# Ejemplo de recodificar con una función
def mayus(texto):
    return(texto.upper())

print(df.Status.map(mayus))

# MODIFICAR TEXTOS
# PRINCIPALES ACCESSORS DE TIPO TEXTO

# Usaremos la variable use de df para los ejemplos. Por comodidad vamos a guardarla en una variable propia y sólo con 5 registros.

texto = df.Use[0:5]
print(texto)

print(texto.str.upper()) # mayúsculas
print(texto.str.lower()) # minúsculas
print(texto.str.capitalize()) # estilo frase
print(texto.str.title()) # cada inicio de palabra la primera letra en mayúscula
print(texto.str.cat()) # concatenar
print(texto.str.join(sep = '--')) # unir cada elemento del texto por un separadorprint(
print(texto.str.split()) # separar el texto

# Comprobar si contiene algún subtexto en concreto, se usa mucho para filtrar variables

filtro = df.columns.str.startswith('Funded')
print(df.loc[:,filtro])

# Comprobar si contiene

filtro = df.columns.str.contains(('Funded'))
print(df.loc[:,filtro])

# Comprobar si termina por

filtro = df.columns.str.endswith('Amount')
print(df.loc[:,filtro])

print(texto.str.len()) # calcular la longitud de un texto
print(df.columns.str.replace(pat = ' ', repl = '_')) # reemplazar valor de un texto
print(texto.str.strip()) # encontrar valor (devuelve la posición de la primera ocurrencia, y si no lo encuentra -1)

# Encontrar espacios delante o detrás del texto con split()

