print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("*********************************")
print("IMPORTACIÓN DE DATOS - EJERCICIOS")
print("*********************************")

import pandas as pd
import numpy as np 

# Documentación de Pandas https://pandas.pydata.org/pandas-docs/stable/reference/index.html

print(pd.options.display.min_rows) # por defecto muestra 10 (5 superiores y 5 inferiore)

# %config IPCompleter.greedy = True # para autocompletar cuando trabajamos con notebook
pd.options.display.min_rows = 6 # por defecto nos muestra 6 registros
print(pd.options.display.min_rows)

print("***********")
print("EJERCICIO 1")
print("***********")

# Importa con read_csv y sin usar ningún parámetro adicional al nombre del archivo. Y usa .info() para revisar los tipos de las variables

df = pd.read_csv("../../../00_DATASETS/Historico_IBEX35_Diario.csv")

print(df.head())
df.info()

# Algunas conclusiones sobre la importación:

# - Separa bien los campos
# - Coge bien los nombres de variables, tienen acentos y símbolos así que nos interesa cambiarlos
# - Importa todas las variables como objeto
# - La fecha debería ser el índice. 

print("***********")
print("EJERCICIO 2")
print("***********")

# Antes de seguir importa unas cuantas líneas como texto bruto para ver lo que contiene realmente el fichero.

previa = open("../../../00_DATASETS/Historico_IBEX35_Diario.csv","r")
print(previa.readlines()[0:10])
previa.close()

print("***********")
print("EJERCICIO 3")
print("***********")

# Vamos a ir paso a paso. Comenzamos por corregir los nombres.
# Pásale como una lista los mismos nombres pero quitando acentos y símbolos, y todo en minúscula

cabecera = ['fecha','ultimo','apertura','maximo','minimo','vol','var']

df = pd.read_csv("../../../00_DATASETS/Historico_IBEX35_Diario.csv",
                        sep = ',',
                        header = 0,
                        names = cabecera) # skiprows ahora es 2 porque sino importará la fila 84

print(df)

print("***********")
print("EJERCICIO 4")
print("***********")

# En este dataset parece que tiene sentido que la Fecha sea el index.
# Así que dile que lo parsee como una fecha y que la ponga como índice.

df = pd.read_csv("../../../00_DATASETS/Historico_IBEX35_Diario.csv", 
            sep = ',',
            header = 0,
            names = cabecera,
            parse_dates = ['fecha'])

print(df)
df.info()

df.set_index("fecha", inplace = True)
print(df)

print("***********")
print("EJERCICIO 5")
print("***********")

# Ahora soluciona el tema del separador de decimales y el separador de miles.
# Muestra la tabla y los tipos de variables.

df = pd.read_csv("../../../00_DATASETS/Historico_IBEX35_Diario.csv", 
            sep = ",",
            header = 0,
            names = cabecera,
            decimal = ",",
            thousands = ".",
            parse_dates = ['fecha'])

print(df)
df.info()

df.set_index("fecha", inplace = True)
print(df)

print("***********")
print("EJERCICIO 6")
print("***********")

# Ya nos coge todo como número menos vol y var porque tienen los símpbolos de M y %.
# Como ya no podemos hacer más en la importación los dejamos así y ya los corregiremos posteriormente.

# Pero también vemos que vol tiene nulos representados como un guión, así que introduce una última modificación para que entienda que los guiones son nulos.

df = pd.read_csv("../../../00_DATASETS/Historico_IBEX35_Diario.csv", 
            sep = ",",
            header = 0,
            names = cabecera,
            decimal = ",",
            thousands = ".",
            na_values ="-",
            parse_dates = ['fecha'])

print(df)
df.info()

df.set_index("fecha", inplace = True)
print(df)

print("***********")
print("EJERCICIO 7")
print("***********")

# IMPORTACIÓN DE BASE DE DATOS

# 1. Cargar los paquetes necesarios
import sqlalchemy as sa

# 2. Establecer una conexión con la base de datos
connection = sa.create_engine("sqlite:///../../../00_DATASETS/chinook.db") 

# 3. Hacer una consulta genérica en SQL 
t_invoices = pd.read_sql("SELECT * FROM invoices", connection)

# 4. Traer los datos a Pandas y trabajar normalmente
print(t_invoices)

t_invoices = pd.read_sql("SELECT * FROM invoice_items", connection)
print(t_invoices)


