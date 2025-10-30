---
title: Gestionar datos de archivos Excel con Golang mediante C++
linktitle: Datos de celdas
type: docs
weight: 110
url: /es/go-cpp/view-and-edit-excel-data/
description: Este artículo describe cómo ver y editar datos de archivos de Excel con la biblioteca Aspose.Cells usando C++.
keywords: Aspose.Cells C++ Administrar datos de archivos de Excel, agregar datos a archivos de Excel, obtener datos de archivos de Excel, cómo mejorar la eficiencia al agregar datos, administrar datos de celdas, actualizar datos de celdas, obtener datos de celdas, insertar datos en celdas
---

{{% alert color="primary" %}}

En [Accediendo a Celdas de una Hoja de Cálculo](/cells/es/cpp/accediendo-a-celdas-de-una-hoja-de-calculo/), discutimos enfoques básicos para acceder a celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a celdas.

{{% /alert %}}

## **Cómo agregar datos a las celdas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells permite a los desarrolladores agregar datos a las celdas en hojas de cálculo llamando al método [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/) de la clase [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). Aspose.Cells proporciona versiones sobrecargadas del método [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/) que permiten a los desarrolladores agregar diferentes tipos de datos a las celdas. Utilizando estas versiones sobrecargadas del método [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/), es posible agregar un valor Booleano, cadena, doble, entero o de fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData.go" >}}
## **Cómo mejorar la eficiencia**

Si usas el método [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue_bool/) para ingresar una gran cantidad de datos a una hoja de cálculo, debes agregar valores a las celdas primero por filas y luego por columnas. Este enfoque mejora considerablemente la eficiencia de tus aplicaciones.

## **Cómo recuperar datos de las celdas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite el acceso a hojas de cálculo en el archivo. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La clase [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) proporciona varias propiedades que permiten a los desarrolladores recuperar valores de las celdas de acuerdo a sus tipos de datos. Estas propiedades incluyen:

- [**StringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/): devuelve el valor de cadena de la celda.
- [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/): devuelve el valor doble de la celda.
- [**BoolValue**](https://reference.aspose.com/cells/go-cpp/cell/getboolvalue/): devuelve el valor booleano de la celda.
- [**DateTimeValue**](https://reference.aspose.com/cells/go-cpp/cell/getdatetimevalue/): devuelve el valor de fecha/hora de la celda.
- [**FloatValue**](https://reference.aspose.com/cells/go-cpp/cell/getfloatvalue/): devuelve el valor de punto flotante de la celda.
- [**IntValue**](https://reference.aspose.com/cells/go-cpp/cell/getintvalue/): devuelve el valor entero de la celda.

Cuando un campo no está lleno, las celdas con [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/) o [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) lanzan una excepción.

También se puede verificar el tipo de datos contenido en una celda utilizando la propiedad [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) de la clase [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). De hecho, la propiedad [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) de la clase [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) se basa en la enumeración [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) cuyos valores predefinidos se enumeran a continuación:

|**Tipos de Valor de Celda**|**Descripción**|
| :- | :- |
|IsBool|Especifica que el valor de la celda es Booleano.|
|IsDateTime|Especifica que el valor de la celda es fecha/hora.|
|IsNull|Representa una celda en blanco.|
|IsNumeric|Especifica que el valor de la celda es numérico.|
|IsString|Especifica que el valor de la celda es una cadena de texto.|
|IsUnknown|Especifica que el valor de la celda es desconocido.|

También puedes utilizar los tipos de valor de celda predefinidos anteriores para comparar con el tipo de datos presente en cada celda.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData-1.go" >}}
{{% alert color="primary" %}}

Mientras trabajas en hojas de cálculo, los usuarios pueden agregar diferentes tipos de datos en las celdas. Estos tipos de datos pueden incluir valores booleanos, enteros, de punto flotante, texto o fecha/hora. Con Aspose.Cells, puedes obtener los valores apropiados de las celdas de acuerdo a sus tipos de datos.

{{% /alert %}}

## **Temas avanzados**
- [Accediendo a celdas de una hoja de cálculo](/cells/es/cpp/accessing-cells-of-a-worksheet/)
- [Convertir datos numéricos de texto a número](/cells/es/cpp/convert-text-numeric-data-to-number/)
- [Crear subtotales](/cells/es/cpp/creating-subtotals/)
- [Filtrado de datos](/cells/es/cpp/data-filtering/)
- [Ordenación de datos](/cells/es/cpp/sort-data-of-excel/)
- [Validación de datos](/cells/es/cpp/data-validation/)
- [Buscar o buscar datos](/cells/es/cpp/find-or-search-data/)
- [Obtener el valor de cadena de celda con y sin formato](/cells/es/cpp/get-cell-string-value-with-and-without-formatting/)
- [Añadir Texto Enriquecido HTML dentro de la Celda](/cells/es/cpp/adding-html-rich-text-inside-the-cell/)
- [Insertar hipervínculos en Excel u OpenOffice](/cells/es/cpp/insert-hyperlinks-to-excel/)
- [Cómo y dónde utilizar enumeradores](/cells/es/cpp/how-and-where-to-use-enumerators/)
- [Medir el ancho y alto del valor de la celda en unidades de píxeles](/cells/es/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lectura de valores de celda en múltiples hilos simultáneamente](/cells/es/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversión entre el nombre de la celda y el índice de fila/columna](/cells/es/cpp/names-and-indices/)
- [Poblar datos primero por fila luego por columna](/cells/es/cpp/populate-data-first-by-row-then-by-column/)
- [Preservar el prefijo de comilla simple del valor de la celda o rango](/cells/es/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Acceder y actualizar partes de texto enriquecido de la celda](/cells/es/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
