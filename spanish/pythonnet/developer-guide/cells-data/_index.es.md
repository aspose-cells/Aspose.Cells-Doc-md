---
title: Gestionar datos de archivos de Excel
linktitle: Datos de celdas
type: docs
weight: 110
url: /es/python-net/view-and-edit-excel-data/
description: Este artículo describe cómo ver y editar datos de archivos de Excel con la biblioteca Aspose.Cells for Python via .NET.
keywords: Biblioteca de Excel de Python, Aspose.Cells for Python. Gestionar datos de archivos de Excel, agregar datos de Python a archivos de Excel, obtener datos de archivos de Excel con Python, cómo mejorar la eficiencia de la adición de datos con Python, gestionar datos de celdas en Python, actualizar datos de celdas en Python, obtener datos de celdas en Python, insertar datos de celdas en Python.
---

{{% alert color="primary" %}}

En [Cómo acceder a celdas de una hoja de cálculo](/cells/es/python-net/accessing-cells-of-a-worksheet/), discutimos enfoques básicos para acceder a celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a las celdas.

{{% /alert %}}

## **Cómo agregar datos a las celdas**

Aspose.Cells for Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección de [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección de [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Cada elemento en la colección de [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells for Python via .NET permite a los desarrolladores agregar datos a las celdas en hojas de cálculo llamando al método [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Aspose.Cells for Python via .NET proporciona versiones sobrecargadas del método [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) que permiten a los desarrolladores agregar diferentes tipos de datos a las celdas. Usando estas versiones sobrecargadas del método [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int), es posible agregar valores booleanos, cadenas, números de punto flotante, enteros o fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **Cómo mejorar la eficiencia**

Si usas el método [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) para ingresar una gran cantidad de datos a una hoja de cálculo, debes agregar valores a las celdas primero por filas y luego por columnas. Este enfoque mejora considerablemente la eficiencia de tus aplicaciones.

## **Cómo recuperar datos de las celdas**

Aspose.Cells for Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección de [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) que permite acceder a hojas de cálculo en el archivo. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección de [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Cada elemento en la colección de [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

La clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) proporciona varias propiedades que permiten a los desarrolladores recuperar valores de las celdas de acuerdo a sus tipos de datos. Estas propiedades incluyen:

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): devuelve el valor de cadena de la celda.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): devuelve el valor doble de la celda.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): devuelve el valor booleano de la celda.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): devuelve el valor de fecha/hora de la celda.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): devuelve el valor de punto flotante de la celda.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): devuelve el valor entero de la celda.

Cuando un campo no está lleno, las celdas con [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) o [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) lanzan una excepción.

También se puede verificar el tipo de datos contenido en una celda utilizando la propiedad [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). De hecho, la propiedad [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) se basa en la enumeración [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype) cuyos valores predefinidos se enumeran a continuación:

|**Tipos de Valor de Celda**|**Descripción**|
| :- | :- |
|IS_BOOL|Especifica que el valor de la celda es Booleano.
|IS_DATE_TIME|Especifica que el valor de la celda es fecha/hora.
|IS_NULL|Representa una celda en blanco.
|IS_NUMERIC|Especifica que el valor de la celda es numérico.
|IS_STRING|Especifica que el valor de la celda es una cadena de texto.
|IS_ERROR|Especifica que el valor de la celda es un valor de error.
|IS_UNKNOWN|Especifica que el valor de la celda es desconocido.

También puedes utilizar los tipos de valor de celda predefinidos anteriores para comparar con el tipo de datos presente en cada celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

Mientras se trabaja en hojas de cálculo, los usuarios pueden agregar diferentes tipos de datos en las celdas. Estos tipos de datos pueden incluir valores booleanos, enteros, de punto flotante, de texto o de fecha/hora. Con Aspose.Cells para Python via .NET, puedes obtener los valores apropiados de las celdas de acuerdo a sus tipos de datos.

{{% /alert %}}

## **Temas avanzados**
- [Accediendo a celdas de una hoja de cálculo](/cells/es/python-net/accessing-cells-of-a-worksheet/)
- [Convertir datos numéricos de texto a número](/cells/es/python-net/convert-text-numeric-data-to-number/)
- [Crear subtotales](/cells/es/python-net/creating-subtotals/)
- [Filtrado de datos](/cells/es/python-net/data-filtering/)
- [Ordenación de datos](/cells/es/python-net/sort-data-of-excel/)
- [Validación de datos](/cells/es/python-net/data-validation/)
- [Obtener el valor de cadena de celda con y sin formato](/cells/es/python-net/get-cell-string-value-with-format-strategy/)
- [Añadir Texto Enriquecido HTML dentro de la Celda](/cells/es/python-net/adding-html-rich-text-inside-the-cell/)
- [Buscar o buscar datos](/cells/es/python-net/find-or-search-data/)
- [Insertar hipervínculos en Excel u OpenOffice](/cells/es/python-net/insert-hyperlinks-to-excel/)
- [Medir el ancho y alto del valor de la celda en unidades de píxeles](/cells/es/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Conversión entre el nombre de la celda y el índice de fila/columna](/cells/es/python-net/names-and-indices/)
- [Poblar datos primero por fila luego por columna](/cells/es/python-net/populate-data-first-by-row-then-by-column/)
- [Preservar el prefijo de comilla simple del valor de la celda o rango](/cells/es/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Acceder y actualizar partes de texto enriquecido de la celda](/cells/es/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="python-net" >}}
