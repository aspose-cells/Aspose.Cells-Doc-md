---
title: Convertir Excel a NumPy
type: docs
weight: 30
url: /es/python-net/convert-excel-to-numpy/
description: Convertir Excel a NumPy utilizando la API de Aspose.Cells para Python via .NET.
keywords: Convertir Excel de Python a un array de NumPy, Exportar libro de trabajo a un array de NumPy en Python via NET, Convertir Fila de Python a un array de NumPy, Convertir Tabla de Python a un array de NumPy, Exportar ListObject a un array de NumPy en Python via NET, Convertir rango de Python a un array de NumPy, Columna a un array de NumPy usando Python.
---

## **Introducción a NumPy**
NumPy (Numerical Python) es una extensión de cálculo numérico de código abierto de Python. Esta herramienta se puede utilizar para almacenar y procesar matrices grandes, que es mucho más eficiente que la estructura de listas anidadas de Python (que también se puede utilizar para representar matrices). Admite una gran cantidad de matrices dimensionales y operaciones de matrices, y también proporciona una gran cantidad de bibliotecas de funciones matemáticas para operaciones de matriz. 

Las principales funciones de NumPy:
1. Ndarray, un objeto de matriz multidimensional, es una estructura de datos rápida, flexible y que ahorra espacio.
1. Operaciones de álgebra lineal, incluyendo multiplicación de matrices, transposición, inversión, etc.
1. Transformada de Fourier, realizando una transformada rápida de Fourier en una matriz.
1. Operación rápida de matrices de punto flotante.
1. Integrar código en lenguaje C en Python para que se ejecute más rápido.

Usando la API de Aspose.Cells for Python via .NET, puedes convertir Excel, TSV, CSV, Json y muchos otros formatos a Numpy ndarray.

## **Cómo convertir un libro de trabajo de Excel a Numpy ndarray**
Aquí tienes un ejemplo de fragmento de código para demostrar cómo exportar datos de Excel a un array de NumPy usando Aspose.Cells for Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Recorrer los datos de Excel y exportarlos a un Numpy ndarray usando Aspose.Cells for Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

El resultado de la salida:
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **Cómo convertir una hoja de cálculo a Numpy ndarray**
Aquí tienes un ejemplo de fragmento de código para demostrar cómo exportar datos de una hoja de cálculo a un array de Numpy usando Aspose.Cells for Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Convertir datos de la hoja de cálculo a Numpy ndarray usando la biblioteca de Excel Aspose.Cells for Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

El resultado de la salida:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **Cómo convertir un rango de Excel a Numpy ndarray**
Aquí tienes un ejemplo de fragmento de código para demostrar cómo exportar datos de un rango a Numpy ndarray usando Aspose.Cells for Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Crear el rango.
1. Convertir datos de rango a Numpy ndarray usando la biblioteca de Excel Aspose.Cells for Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

El resultado de la salida:
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **Cómo convertir un objeto de lista de Excel a Numpy ndarray**
Aquí tienes un ejemplo de fragmento de código para demostrar cómo exportar datos de ListObject a un ndarray de NumPy utilizando Aspose.Cells for Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Crear objeto ListObject.
1. Convertir datos de ListObject a ndarray de NumPy utilizando la biblioteca de Excel Aspose.Cells para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

El resultado de la salida:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **Cómo convertir una fila de Excel a ndarray de NumPy**
Aquí tienes un ejemplo de fragmento de código para demostrar cómo exportar datos de fila a ndarray de NumPy utilizando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Obtener objeto de fila por índice de fila.
1. Convertir datos de fila a ndarray de NumPy utilizando la biblioteca de Excel Aspose.Cells para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

El resultado de la salida:
```
['Detroit' 'Central' '3074']
```

## **Cómo convertir una columna de Excel a ndarray de NumPy**
Aquí tienes un ejemplo de fragmento de código para demostrar cómo exportar datos de columna a ndarray de NumPy utilizando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Obtener objeto de columna por índice de columna.
1. Convertir datos de columna a ndarray de NumPy utilizando la biblioteca de Excel Aspose.Cells para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

El resultado de la salida:
```
['Store' '3055' '3036' '3074']
```
