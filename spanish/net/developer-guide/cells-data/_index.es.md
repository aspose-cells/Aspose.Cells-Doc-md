---
title: Gestionar datos de archivos de Excel
linktitle: Datos de celdas
type: docs
weight: 110
url: /es/net/view-and-edit-excel-data/
description: Este artículo describe cómo ver y editar datos de archivos de Excel con la biblioteca Aspose.Cells.
keywords: Gestionar datos de archivos de Excel en C# de Aspose.Cells, agregar datos a archivos de Excel, obtener datos de archivos de Excel, Cómo mejorar la eficiencia de agregar datos, gestionar datos de celdas, actualizar datos de celdas, obtener datos de celdas, insertar datos de celdas
---

{{% alert color="primary" %}}

En [Acceso a celdas de una hoja de cálculo](/cells/es/net/accessing-cells-of-a-worksheet/), discutimos enfoques básicos para acceder a celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a celdas.

{{% /alert %}}

## **Cómo agregar datos a las celdas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells permite a los desarrolladores agregar datos a las celdas en hojas de cálculo llamando al método [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Aspose.Cells proporciona versiones sobrecargadas del método [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) que permiten a los desarrolladores agregar diferentes tipos de datos a las celdas. Utilizando estas versiones sobrecargadas del método [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index), es posible agregar un valor Booleano, cadena, doble, entero o de fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Cómo mejorar la eficiencia**

Si usas el método [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) para ingresar una gran cantidad de datos a una hoja de cálculo, debes agregar valores a las celdas primero por filas y luego por columnas. Este enfoque mejora considerablemente la eficiencia de tus aplicaciones.

## **Cómo recuperar datos de las celdas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite el acceso a hojas de cálculo en el archivo. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

La clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) proporciona varias propiedades que permiten a los desarrolladores recuperar valores de las celdas de acuerdo a sus tipos de datos. Estas propiedades incluyen:

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): devuelve el valor de cadena de la celda.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): devuelve el valor doble de la celda.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): devuelve el valor booleano de la celda.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): devuelve el valor de fecha/hora de la celda.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): devuelve el valor de punto flotante de la celda.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): devuelve el valor entero de la celda.

Cuando un campo no está lleno, las celdas con [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) o [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) lanzan una excepción.

También se puede verificar el tipo de datos contenido en una celda utilizando la propiedad [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). De hecho, la propiedad [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) se basa en la enumeración [**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype) cuyos valores predefinidos se enumeran a continuación:

|**Tipos de Valor de Celda**|**Descripción**|
| :- | :- |
|IsBool|Especifica que el valor de la celda es Booleano.|
|IsDateTime|Especifica que el valor de la celda es fecha/hora.|
|IsNull|Representa una celda en blanco.|
|IsNumeric|Especifica que el valor de la celda es numérico.|
|IsString|Especifica que el valor de la celda es una cadena de texto.|
|IsUnknown|Especifica que el valor de la celda es desconocido.|

También puedes utilizar los tipos de valor de celda predefinidos anteriores para comparar con el tipo de datos presente en cada celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Mientras trabajas en hojas de cálculo, los usuarios pueden agregar diferentes tipos de datos en las celdas. Estos tipos de datos pueden incluir valores booleanos, enteros, de punto flotante, texto o fecha/hora. Con Aspose.Cells, puedes obtener los valores apropiados de las celdas de acuerdo a sus tipos de datos.

{{% /alert %}}

## **Temas avanzados**
- [Accediendo a celdas de una hoja de cálculo](/cells/es/net/accessing-cells-of-a-worksheet/)
- [Convertir datos numéricos de texto a número](/cells/es/net/convert-text-numeric-data-to-number/)
- [Crear subtotales](/cells/es/net/creating-subtotals/)
- [Filtrado de datos](/cells/es/net/data-filtering/)
- [Ordenación de datos](/cells/es/net/sort-data-of-excel/)
- [Validación de datos](/cells/es/net/data-validation/)
- [Exportar datos desde la hoja de cálculo](/cells/es/net/export-data-from-worksheet/)
- [Buscar o buscar datos](/cells/es/net/find-or-search-data/)
- [Obtener el valor de cadena de celda con y sin formato](/cells/es/net/get-cell-string-value-with-and-without-formatting/)
- [Añadir Texto Enriquecido HTML dentro de la Celda](/cells/es/net/adding-html-rich-text-inside-the-cell/)
- [Insertar hipervínculos en Excel u OpenOffice](/cells/es/net/insert-hyperlinks-to-excel/)
- [Importar datos en la hoja de cálculo](/cells/es/net/import-data-into-worksheet/)
- [Cómo y dónde utilizar enumeradores](/cells/es/net/how-and-where-to-use-enumerators/)
- [Medir el ancho y alto del valor de la celda en unidades de píxeles](/cells/es/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lectura de valores de celda en múltiples hilos simultáneamente](/cells/es/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversión entre el nombre de la celda y el índice de fila/columna](/cells/es/net/names-and-indices/)
- [Poblar datos primero por fila luego por columna](/cells/es/net/populate-data-first-by-row-then-by-column/)
- [Preservar el prefijo de comilla simple del valor de la celda o rango](/cells/es/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Acceder y actualizar partes de texto enriquecido de la celda](/cells/es/net/access-and-update-the-portions-of-rich-text-of-cell/)



{{< app/cells/assistant language="csharp" >}}
