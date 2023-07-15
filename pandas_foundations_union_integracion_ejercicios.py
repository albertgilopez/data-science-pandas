print("******************")
print("PANDAS FOUNDATIONS")
print("******************")

print("***************************************************")
print("CALIDAD DE DATOS - UNIÓN E INTEGRACIÓN - EJERCICIOS")
print("***************************************************")

import pandas as pd 
import numpy as np 

import sqlalchemy as sa

# Documentación de Pandas https://pandas.pydata.org/pandas-docs/stable/reference/index.html

print(pd.options.display.min_rows) # por defecto muestra 10 (5 superiores y 5 inferiore)

# %config IPCompleter.greedy = True # para autocompletar cuando trabajamos con notebook
pd.options.display.min_rows = 6 # por defecto nos muestra 6 registros
print(pd.options.display.min_rows)

print("***********")
print("EJERCICIO 1")
print("***********")

# Importa el contenido de la tabla invoices a un objeto que se llame facturas.

# Crear la conexión a la base de datos
engine = sa.create_engine('sqlite:///../../../00_DATASETS/chinook.db')
# Consulta SQL para obtener los datos de la tabla invoices
query = "SELECT * FROM invoices"
# Importar los datos a un objeto DataFrame llamado facturas
facturas = pd.read_sql_query(query, engine)
# Verificar los primeros registros del objeto facturas
print(facturas.head())

print("***********")
print("EJERCICIO 2")
print("***********")

# Crea la tabla variables_izq con las variables de Invoiceid a BillingCity, y comprueba sus dimensiones para ver que está bien.

# Importar los datos de la tabla invoices a un objeto DataFrame
facturas = pd.read_sql_query(query, engine)

# Obtener la mitad izquierda y derecha de las variables
variables_izq = facturas.iloc[:, :int(len(facturas.columns)/2)]
variables_drc = facturas.iloc[:, int(len(facturas.columns)/2):]

# Obtener la mitad superior e inferior de los registros
registros_sup = facturas.iloc[:int(len(facturas)/2), :]
registros_inf = facturas.iloc[int(len(facturas)/2):, :]

# Eliminar la columna de identificador si existe
variables_izq = variables_izq.drop('InvoiceId', axis=1, errors='ignore')
variables_drc = variables_drc.drop('InvoiceId', axis=1, errors='ignore')
registros_sup = registros_sup.drop('InvoiceId', axis=1, errors='ignore')
registros_inf = registros_inf.drop('InvoiceId', axis=1, errors='ignore')

print("***********")
print("EJERCICIO 3")
print("***********")

# Crea la tabla variables_drc con las variables de BillingState a Total, y comprueba sus dimensiones para ver que está bien.

# Crear la tabla variables_drc con las variables de BillingState a Total
variables_drc = facturas.loc[:, "BillingState":"Total"]

# Verificar las dimensiones de la tabla variables_drc
print("Dimensiones de variables_drc:", variables_drc.shape)

print("***********")
print("EJERCICIO 4")
print("***********")

# Crea la tabla registros_sup con los registros del 0 al 206, y comprueba sus dimensiones para ver que está bien.

# Crear la tabla registros_sup con los registros del 0 al 206
registros_sup = facturas.iloc[0:207, :]
# Verificar las dimensiones de la tabla registros_sup
print("Dimensiones de registros_sup:", registros_sup.shape)

print("***********")
print("EJERCICIO 5")
print("***********")

# Crea la tabla registros_inf con los registros del 206 al 412, y comprueba sus dimensiones para ver que está bien.

# Crear la tabla registros_inf con los registros del 206 al 412
registros_inf = facturas.iloc[206:413, :]
# Verificar las dimensiones de la tabla registros_inf
print("Dimensiones de registros_inf:", registros_inf.shape)

print("***********")
print("EJERCICIO 6")
print("***********")

# Crea una única tabla llamada unir_variables uniendo variables_izq con variables_drc, y comprueba sus dimensiones que deberán ser las mismas que en facturas.

# Unir variables_izq y variables_drc en una única tabla
unir_variables = pd.concat([variables_izq, variables_drc], axis=1)

# Verificar las dimensiones de la tabla unir_variables
print("Dimensiones de unir_variables:", unir_variables.shape)
print("Dimensiones de facturas:", facturas.shape)

print(unir_variables.info())
print(facturas.info())

print("***********")
print("EJERCICIO 7")
print("***********")

# Ahora vamos a practicar cruces de tablas.
# Como sabes para ello SI necesitamos un campo clave de unión.
# Si consultas el modelo de datos verás que en nuestras tablas el campo clave es InvoiceId

# Antes que nada carga el contenido de la tabla invoice_items a un objeto que se llame items.

# Cargar el contenido de la tabla invoice_items en un objeto DataFrame llamado items
items = pd.read_sql_query("SELECT * FROM invoice_items", engine)
# Verificar los primeros registros del objeto items
print(items.head())

print("***********")
print("EJERCICIO 8")
print("***********")

# Vamos a familiarizarnos con los datos.
# Saca facturas por pantalla y revisa detalladamente todos sus campos.

# Cargar el contenido de la tabla invoices en un objeto DataFrame llamado facturas
facturas = pd.read_sql_query("SELECT * FROM invoices", engine)
# Mostrar por pantalla las facturas
print(facturas)

# Comprueba si el InvoiceId es único en esta tabla.
# Pista: puedes usar la propiedad is_unique

# Cargar el contenido de la tabla invoices en un objeto DataFrame llamado facturas
facturas = pd.read_sql_query("SELECT * FROM invoices", engine)

# Comprobar si el campo InvoiceId es único
es_unico = facturas['InvoiceId'].is_unique

# Mostrar el resultado
if es_unico:
    print("El campo InvoiceId es único en la tabla invoices.")
else:
    print("El campo InvoiceId no es único en la tabla invoices.")

# Cargar el contenido de la tabla invoice_items en un objeto DataFrame llamado items
items = pd.read_sql_query("SELECT * FROM invoice_items", engine)

# Comprobar si el campo InvoiceId es único en la tabla invoices
es_unico = items['InvoiceId'].is_unique

# Mostrar el resultado
if es_unico:
    print("El campo InvoiceId es único en la tabla invoices.")
else:
    print("El campo InvoiceId no es único en la tabla invoices.")

# InvoiceId no es único en la tabla "invoices" debido a la relación uno a muchos entre facturas e ítems de factura.

print("***********")
print("EJERCICIO 9")
print("***********")

# Quédate en la cabeza con el número de registros que tiene facturas y los que tiene items.
# Haz un inner join entre ambas tablas. Y fíjate en cuantos registros tiene la salida. ¿Qué crees que significa?

# Obtener el número de registros en cada tabla
num_registros_facturas = len(facturas)
num_registros_items = len(items)

# Realizar un inner join entre las tablas facturas e items
resultado = pd.merge(facturas, items, on='InvoiceId', how='inner')

# Obtener el número de registros en la salida del inner join
num_registros_salida = len(resultado)

# Imprimir los números de registros
print("Número de registros en facturas:", num_registros_facturas)
print("Número de registros en items:", num_registros_items)
print("Número de registros en la salida del inner join:", num_registros_salida)

# Al imprimir los números de registros, podrás verificar cuántos registros tiene cada tabla y cuántos registros resultan del inner join.
# Si el número de registros en la salida del inner join es menor que el número de registros en las tablas originales, significa que hay facturas que no tienen elementos de factura asociados en la tabla "items".

print("************")
print("EJERCICIO 10")
print("************")

# Ahora haz un rigth join entre ambas tablas (manda items).
# Y fíjate en cuantos registros tiene la salida. ¿Qué crees que significa?

# Realizar un right join entre las tablas facturas e items
resultado = pd.merge(facturas, items, on='InvoiceId', how='right')

# Obtener el número de registros en la salida del right join
num_registros_salida = len(resultado)

# Imprimir el número de registros en la salida
print("Número de registros en la salida del right join:", num_registros_salida)

# Al imprimir el número de registros en la salida, podrás verificar cuántos registros resultan del right join.
# Si el número de registros es mayor que el número de registros en la tabla "facturas", significa que hay elementos de factura en la tabla "items" que no tienen una factura asociada en la tabla "facturas".

print("************")
print("EJERCICIO 11")
print("************")

# Ahora vamos a crear una nueva tabla llamada facturas2 en la que cogeremos los regitros desde el 100 hasta el final de facturas.
# Creala. Sácala por pantalla y fíjate en cuantos registros tiene. IMPORTANTE: recuerda hacer una copia del original.

# Crear una copia de los registros desde el 100 hasta el final de facturas
facturas2 = facturas[100:].copy()

# Mostrar por pantalla los registros de facturas2
print(facturas2)

# Obtener el número de registros en facturas2
num_registros_facturas2 = len(facturas2)

# Imprimir el número de registros en facturas2
print("Número de registros en facturas2:", num_registros_facturas2)

print("************")
print("EJERCICIO 12")
print("************")

# Haz un inner join entre facturas2 e items y fíjate en cuantos registros tiene, ¿qué ha pasado?

# Realizar un inner join entre las tablas facturas2 e items
resultado = pd.merge(facturas2, items, on='InvoiceId', how='inner')

# Obtener el número de registros en la salida del inner join
num_registros_salida = len(resultado)

# Imprimir el número de registros en la salida
print("Número de registros en la salida del inner join:", num_registros_salida)

# Al imprimir el número de registros en la salida, verás cuántos registros resultan del inner join. 
# Es posible que el número de registros sea menor que el esperado, ya que solo se están considerando los registros de "facturas2" que cumplen con los criterios de filtrado, y aquellos registros de "items" que tengan una correspondencia en "facturas2" en función del campo "InvoiceId".

print("************")
print("EJERCICIO 13")
print("************")

# Ahora haz un rigth join entre ambas tablas (manda items). # Y fíjate en cuantos registros tiene la salida.
# ¿Qué ha pasado? ¿Por qué sale diferenete número de registros que con el inner join si cuando hicimos lo mismo con facturas salía igual?

# Realizar un right join entre las tablas facturas2 e items
resultado = pd.merge(facturas2, items, on='InvoiceId', how='right')

print(resultado) # aparecen nulos porque el right join obliga a coge lo registros

# Obtener el número de registros en la salida del right join
num_registros_salida = len(resultado)

# Imprimir el número de registros en la salida
print("Número de registros en la salida del right join:", num_registros_salida)

# Al imprimir el número de registros en la salida, notarás que es mayor que el número de registros en el inner join. 
# Esto se debe a que el right join mantiene todos los registros de "items", incluso aquellos que no tienen una correspondencia en "facturas2".

print("************")
print("EJERCICIO 14")
print("************")

# Hasta ahora hemos estado uniendo 2 tablas, pero ¿qué pasa si queremos unir más?
# La aproximación más sencilla es ir uniendo en tablas temporales y al final borrarlas.
# Por ejemplo, como siguiente paso importa la tabla customers a un objeto que se llame clientes.

# Importar el contenido de la tabla customers a un objeto DataFrame llamado clientes
clientes = pd.read_sql_query("SELECT * FROM customers", engine)

# Crear una tabla temporal llamada temp_facturas que contenga los registros de facturas
facturas.to_sql('temp_facturas', engine, if_exists='replace', index=False)

# Crear una tabla temporal llamada temp_items que contenga los registros de items
items.to_sql('temp_items', engine, if_exists='replace', index=False)

# Realizar la unión de las tablas facturas, items y customers utilizando las tablas temporales

# Realizar los left joins entre las tablas clientes, facturas e items
final = pd.merge(clientes, facturas, on='CustomerId', how='left')
final = pd.merge(final, items, on='InvoiceId', how='left')

# Mostrar por pantalla los registros de final
print(final)

print("************")
print("EJERCICIO 15")
print("************")

# Borra la tabla temporal que has tenido que crear para que no ocupe memoria.
# Pista: puedes usar el comando del de Python.

del final

# Cerrar la conexión a la base de datos
engine.dispose()
