---
title: Gestionar datos de archivos de Excel
linktitle: Datos de celdas
type: docs
weight: 110
url: /es/nodejs-cpp/view-and-edit-excel-data/
description: Este artículo describe cómo ver y editar datos de archivos Excel con la biblioteca Aspose.Cells para Node.js vía C++.
keywords: Aspose.Cells Node.js vía C++, Administrar datos de archivos Excel, agregar datos a archivos Excel, obtener datos de archivos Excel, Cómo mejorar la eficiencia al agregar datos, gestionar datos de celdas, actualizar datos de celdas, obtener datos de celdas, insertar datos en celdas
---

{{% alert color="primary" %}}

En [Acceder a las celdas de una hoja de cálculo](/cells/es/nodejs-cpp/accessing-cells-of-a-worksheet/), discutimos métodos básicos para acceder a celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para añadir diferentes tipos de datos a las celdas.

{{% /alert %}}

## **Cómo agregar datos a las celdas**

Aspose.Cells for Node.js via C++ proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección de [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en el archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ofrece una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Aspose.Cells permite a los desarrolladores agregar datos a las celdas en hojas de cálculo llamando al método [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Aspose.Cells proporciona versiones sobrecargadas del método [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) que permiten a los desarrolladores agregar diferentes tipos de datos a las celdas. Usando estas versiones sobrecargadas del método [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-), es posible agregar valores booleanos, cadenas, doble, enteros, o fecha/hora, etc.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **Cómo mejorar la eficiencia**

Si usas el método [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) para poner una gran cantidad de datos en una hoja, deberías agregar valores a las celdas, primero por filas y luego por columnas. Este enfoque mejora mucho la eficiencia de tus aplicaciones.

## **Cómo recuperar datos de las celdas**

Aspose.Cells for Node.js via C++ proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección de [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a las hojas de cálculo en el archivo. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ofrece una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

La clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) proporciona varias propiedades que permiten a los desarrolladores obtener valores de las celdas según sus tipos de datos. Estas propiedades incluyen:

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): devuelve el valor de cadena de la celda.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): devuelve el valor doble de la celda.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): devuelve el valor booleano de la celda.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): devuelve el valor de fecha/hora de la celda.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): devuelve el valor flotante de la celda.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): devuelve el valor entero de la celda.

Cuando un campo no está lleno, las celdas con [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) o [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) generan una excepción.

El tipo de datos contenido en una celda también puede verificarse usando el método [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). De hecho, el método [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) se basa en la enumeración [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype), cuyos valores predefinidos se listan a continuación:

|**Tipos de Valor de Celda**|**Descripción**|
| :- | :- |
|IsBool|Especifica que el valor de la celda es Booleano.|
|IsDateTime|Especifica que el valor de la celda es fecha/hora.|
|IsNull|Representa una celda en blanco.|
|IsNumeric|Especifica que el valor de la celda es numérico.|
|IsString|Especifica que el valor de la celda es una cadena de texto.|
|IsUnknown|Especifica que el valor de la celda es desconocido.|

También puedes utilizar los tipos de valor de celda predefinidos anteriores para comparar con el tipo de datos presente en cada celda.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

Mientras trabajan en hojas de cálculo, los usuarios pueden agregar diferentes tipos de datos en las celdas. Estos tipos de datos pueden incluir valores booleanos, enteros, de punto flotante, texto o fecha/hora. Con Aspose.Cells, puede obtener los valores adecuados de las celdas según sus tipos de datos.

{{% /alert %}}

## **Temas avanzados**
- [Accediendo a celdas de una hoja de cálculo](/cells/es/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [Convertir datos numéricos de texto a número](/cells/es/nodejs-cpp/convert-text-numeric-data-to-number/)
- [Crear subtotales](/cells/es/nodejs-cpp/creating-subtotals/)
- [Filtrado de datos](/cells/es/nodejs-cpp/data-filtering/)
- [Ordenación de datos](/cells/es/nodejs-cpp/sort-data-of-excel/)
- [Validación de datos](/cells/es/nodejs-cpp/data-validation/)
- [Buscar o buscar datos](/cells/es/nodejs-cpp/find-or-search-data/)
- [Obtener el valor de cadena de celda con y sin formato](/cells/es/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [Añadir Texto Enriquecido HTML dentro de la Celda](/cells/es/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [Insertar hipervínculos en Excel u OpenOffice](/cells/es/nodejs-cpp/insert-hyperlinks-to-excel/)
- [Cómo y dónde utilizar enumeradores](/cells/es/nodejs-cpp/how-and-where-to-use-enumerators/)
- [Medir el ancho y alto del valor de la celda en unidades de píxeles](/cells/es/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lectura de valores de celda en múltiples hilos simultáneamente](/cells/es/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversión entre el nombre de la celda y el índice de fila/columna](/cells/es/nodejs-cpp/names-and-indices/)
- [Poblar datos primero por fila luego por columna](/cells/es/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [Preservar el prefijo de comilla simple del valor de la celda o rango](/cells/es/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Acceder y actualizar partes de texto enriquecido de la celda](/cells/es/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
