---
title: Convertir Excel a Datos de Python
type: docs
weight: 30
url: /es/python-net/convert-excel-to-list/
description: Convertir Excel a Lista usando Aspose.Cells para API de Python via .NET.
keywords: Convertir Excel a Diccionario usando la biblioteca de Excel para Python, Convertir Libro a Diccionario usando la biblioteca de Excel para Python, Convertir objeto Fila a Lista usando la biblioteca de Excel para Python, Cómo Convertir ListObject a Lista, Convertir Objeto Columna a Lista usando la biblioteca de Excel para Python, Convertir Rango a Lista usando la biblioteca de Excel para Python, Convertir Hoja de Trabajo a Lista usando la biblioteca de Excel para Python.
---

{{% alert color="primary" %}}

Usando Aspose.Cells para la API de Python via .NET, puedes convertir datos de Excel como Libro, Hoja de Trabajo, Rango, Fila, Columna y otros a lista de Python.

{{% /alert %}}

## **Cómo convertir un libro de Excel a Diccionario**
Aquí tienes un ejemplo de código para demostrar cómo exportar datos de Excel a un diccionario usando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Recorrer todas las hojas de trabajo y convertir el libro a un diccionario usando la biblioteca de Excel para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

El resultado de la salida:
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **Cómo convertir un libro de Excel a Lista**
Aquí tienes un ejemplo de código para demostrar cómo exportar datos de Excel a una lista usando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Recorrer todas las hojas de trabajo y convertir el libro a una lista usando la biblioteca de Excel para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

El resultado de la salida:
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **Cómo convertir una hoja de trabajo a Lista**
Aquí tienes un ejemplo de código para demostrar cómo exportar datos de hoja de trabajo a lista usando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Convertir datos de hoja de trabajo a lista usando la biblioteca de Excel para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

El resultado de la salida:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **Cómo convertir un objeto de lista de Excel a lista**
Aquí tienes un fragmento de código de ejemplo para demostrar cómo exportar datos de ListObject a lista usando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Crear objeto ListObject.
1. Convertir datos de ListObject a lista usando la biblioteca de Excel de Aspose.Cells para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

El resultado de la salida:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **Cómo convertir una fila de Excel a lista**
Aquí tienes un fragmento de código de ejemplo para demostrar cómo exportar datos de fila a lista usando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Obtener objeto de fila por índice de fila.
1. Convertir datos de fila a lista usando la biblioteca de Excel de Aspose.Cells para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

El resultado de la salida:
```
['Detroit', 'Central', 3074]
```

## **Cómo convertir una columna de Excel a lista**
Aquí tienes un fragmento de código de ejemplo para demostrar cómo exportar datos de columna a lista usando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Obtener objeto de columna por índice de columna.
1. Convertir datos de columna a lista usando la biblioteca de Excel Aspose.Cells para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

El resultado de la salida:
```
['Store', 3055, 3036, 3074]
```

## **Cómo convertir un rango de Excel a lista**
Aquí tienes un ejemplo de código para demostrar cómo exportar datos de rango a lista usando Aspose.Cells para Python via .NET:
1. Cargar el [archivo de muestra](sample_data.xlsx).
1. Obtener la primera hoja de cálculo.
1. Crear el rango.
1. Convertir datos del rango a lista usando la biblioteca de Excel Aspose.Cells para Python.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

El resultado de la salida:
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
{{< app/cells/assistant language="python-net" >}}
