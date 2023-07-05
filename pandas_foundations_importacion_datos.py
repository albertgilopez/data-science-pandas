print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("********************")
print("IMPORTACIÓN DE DATOS")
print("********************")

import pandas as pd
import numpy as np 

# Documentación de Pandas https://pandas.pydata.org/pandas-docs/stable/reference/index.html

print(pd.options.display.min_rows) # por defecto muestra 10 (5 superiores y 5 inferiore)

# %config IPCompleter.greedy = True # para autocompletar cuando trabajamos con notebook
pd.options.display.min_rows = 6 # por defecto nos muestra 6 registros
print(pd.options.display.min_rows)

# IMPORTAR DATOS

# COMO IMPORTAR CVS

# read_csv()

# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv

# Parámetros más importantes:

# - sep: separador de campos
# - thousands: separador de miles
# - decimal: separador decimal
# - header: número de línea en el que están los nombres de campos, o None si no hay. Usar 0 si queremos reemplazarlos con names
# - names: lista con los nuevos nombres a usar. Hay que poner el header = 0
# - index_col: la columna que será el índice
# - skiprows: líneas a saltar (comenzando por cero)
# - nrows: número de líneas a leer (para ficheros grandes)
# - parse_dates: lista con las variables que son fechas para que las lea como tipo Datetime64

df = pd.read_csv("../../../00_DATASETS/DataSetKivaCreditScoring.csv", sep = ";", index_col = "id",
					parse_dates = ["Funded Date","Paid Date"])

print(df.head(2))
print(df.info())

# COMO IMPORTAR DE EXCEL

# read_excel()

# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html

# Parámetros más importantes:

# - sheet_name: la hoja a importar, puede ser por posición (empezando en 0) o por nombre
# - header: número de línea en el que están los nombres de campos. Usar 0 si queremos reemplazarlos con names
# - names: lista con los nuevos nombres a usar. Hay que poner el header = 0
# - index_col: la columna que será el índice
# - skiprows: líneas a saltar (comenzando por cero)
# - nrows: número de líneas a leer (para ficheros grandes)
# - parse_dates: lista con las variables que son fechas para que las lea como tipo fecha

df_excel = pd.read_excel("../../../00_DATASETS/DataSetKivaCreditScoring.xlsx", sheet_name = 1, index_col = "id",
					parse_dates = ["Funded Date","Paid Date"]) # solo podemos importar por hojas (le indicamos el número de hoja o el nombre)

print(df_excel.head(2))
print(df_excel.info())

# COMO IMPORTAR DEL PORTAPAPELES

# read_clipboard() (es interesante usarlo para copiar datos de prueba, poca aplicación en entorno empresarial)

# Lógicamente hay que tener algo copiado en el portapapeles

# https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html

# Parámetros más importantes:

# - sep: separador de campos

df_clipboard = pd.read_clipboard(header = None) # se pueden utilizar argumentos de la función read_csv()

print(df_clipboard.head(2))
print(df_clipboard.info())

# COMO IMPORTAR DESDE UNA BASE DE DATOS

# Documentación diferentes conexiones a bases de datos: https://docs.sqlalchemy.org/en/14/core/engines.html

# El proceso estándard sería:

# 1. Cargar los paquetes necesarios
import sqlalchemy as sa

# 2. Establecer una conexión con la base de datos
connection = sa.create_engine("sqlite:///../../../00_DATASETS/chinook.db") 

# 3. Hacer una consulta genérica en SQL 
df_sql = pd.read_sql("SELECT * FROM customers", connection)

# 4. Traer los datos a Pandas y trabajar normalmente
print(df_sql.head())

# GUARDAR DATOS

# to_csv()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

# Parámetros más importantes:

# - path: la ruta para guardar el archivo (incluyendo el nombre)
# - sep: separador de campos
# - decimal: separador decimal
# - index: si guardar el índice o no
# - header: si guardar el nombre de columnas o no

df.to_csv("Prueba.csv")

# to_excel()

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

# Parámetros más importantes:

# - excel_writer: la ruta para guardar el archivo (incluyendo el nombre)
# - sheet_name: nombre de la hoja en la que poner el dataset
# - header: si guardar el nombre de columnas o no
# - index: si guardar el índice o no

# Para evitar un problema: ValueError: Excel does not support datetimes with timezones. Please ensure that datetimes are timezone unaware before writing to Excel.

# Convert the datetime column to timezone unaware
df['Paid Date'] = df['Paid Date'].dt.tz_localize(None)
df['Funded Date'] = df['Funded Date'].dt.tz_localize(None)

# Write the data to Excel
df.to_excel("Prueba.xlsx", index = False)

print(df.head(2))
print(df.info())

# PROBLEMAS Y CASUÍSTICAS HABITUALES DE LA IMPORTACIÓN DE DATOS

# SEPARADOR DE CAMPOS NO ESTÁNDAR

print(pd.read_csv('../../../00_DATASETS/DataSetKivaCreditScoring_problemas.txt', sep = '\t').head(5)) # \t es el carácter ASCII para el tabulador

# También podemos usar herramientas como https://www.ultraedit.com/es/

# PRIMERAS LÍNEAS SIN DATOS VÁLIDOS

# Esto es frecuente en archivos que provienen de Excel, donde al principio de las hojas se suelen poner metadatos como la fecha, título del informe, etc.

print(pd.read_csv('../../../00_DATASETS/DataSetKivaCreditScoring_problemas.txt', sep = '\t', skiprows = 3).head(5))

# COLUMNAS SIN NOMBRE

# Los datos vienen sin cabecera, posiblemente porque los nombres de campos estén en la documentación o metadatos.
# Por tanto debemos evitar que nos cargue la primera línea de datos como los nombres de campos.

# - Si sabemos los nombres y los queremos poner en la importación tenemos que poner header = 0 y los nombres en el parámetro names
# - Si no los sabemos o los queremos poner después simpelmente ponemos header = None

cabecera = ['id','Funded Date','Funded Amount','Country','Country Code','Loan Amount','Paid Date','Paid Amount','Activity','Sector','Delinquent','Name','Use','Status']

print(pd.read_csv('../../../00_DATASETS/DataSetKivaCreditScoring_problemas.txt',
				sep = '\t',
				skiprows = 2,
				header = 0,
				names = cabecera).head(5)) # skiprows ahora es 2 porque sino importará la fila 84

# NULOS NO HABITUALES

# En algunos casos se han podido sustituir ya por algún tipo de código que Pandas no entenderá por defecto como un nulo.
# Aún así, podemos especificarle a Pandas lo que tiene que entender como nulos con el parámetro na_values.

cabecera = ['id','Funded Date','Funded Amount','Country','Country Code','Loan Amount','Paid Date','Paid Amount','Activity','Sector','Delinquent','Name','Use','Status']

pd.read_csv('../../../00_DATASETS/DataSetKivaCreditScoring_problemas.txt', 
            sep = '\t',
            skiprows = 2,
            header = 0,
            names = cabecera,
            na_values = -999).head(5)

# SEPARADOR DECIMAL EUROPEO

cabecera = ['id','Funded Date','Funded Amount','Country','Country Code','Loan Amount','Paid Date','Paid Amount','Activity','Sector','Delinquent','Name','Use','Status']

pd.read_csv('../../../00_DATASETS/DataSetKivaCreditScoring_problemas.txt', 
            sep = '\t',
            skiprows = 2,
            header = 0,
            names = cabecera,
            na_values = -999,
            decimal = ',').info() # o thousands = "." para miles

# IMPORTAR SOLO PARTE DE LOS DATOS

cabecera = ['id','Funded Date','Funded Amount','Country','Country Code','Loan Amount','Paid Date','Paid Amount','Activity','Sector','Delinquent','Name','Use','Status']

pd.read_csv('../../../00_DATASETS/DataSetKivaCreditScoring_problemas.txt', 
            sep = '\t',
            skiprows = 2,
            header = 0,
            names = cabecera,
            na_values = -999,
            nrows = 5)

# PROBLEMAS CON LAS FECHAS

# Es posible que nos importe las fechas como cadenas de texto.
# Así que el primer paso es decirle qué variables queremos que nos importe como fechas.
# Con el parámetro parse_dates y pasándolo como lista todas las variables que sean fechas.

# - Si la fecha estuviera en un formato que no entendiera podemos intentar forzarle poniendo infer_datetime_format a True.
# - Si la fecha está en estilo europeo (primero el día y luego el mes) se puede liar, por ej 02/04 no sabe si es el 2 de Abril o el 4 de Febrero. Entonces tendríamos que ponerle dayfirst = True para que sepa que 02 es el día.
# - Si tras todo esto no conseguirmos importar bien la fecha lo mejor es dejarla como cadena en la importación y ya trabajaremos sobre ella después.

cabecera = ['id','Funded Date','Funded Amount','Country','Country Code','Loan Amount','Paid Date','Paid Amount','Activity','Sector','Delinquent','Name','Use','Status']

pd.read_csv('../../../00_DATASETS/DataSetKivaCreditScoring_problemas.txt', 
            sep = '\t',
            skiprows = 2,
            header = 0,
            names = cabecera,
            na_values = -999,
            parse_dates = ['Funded Date','Paid Date']).info()

# COMO PREVISUALIZAR UN ARCIVO

# En un mundo ideal tendremos documentación o metadatos del archivo en algún sitio. O muy probablemente alguien haya hecho esa extracción o haya ya manejado esos datos.
# Además de lo que hemos ido viendo, podemos abrir el archivo en modo lectura y extraer un conjunto de líneas que nos sirva como muestra.

# - Abrimos el archivo con open
# - Leemos un número de líneas con readlines. Devuelve una lista así que podemos hacer slice para sacar las que quereamos
# - Cerramos el archivo (es buena práctica no dejarlos abiertos)

# Por ejemplo en nuestro caso, esta vista previa de 10 líneas nos ayuda a ver que:

# - Los datos no empiezan en la primera fila
# - No vienen nombres de campos
# - El separador de campos es el tabulador (\t)
# - ...

previa = open('../../../00_DATASETS/DataSetKivaCreditScoring_problemas.txt','r')
print(previa.readlines()[0:10])
previa.close()

