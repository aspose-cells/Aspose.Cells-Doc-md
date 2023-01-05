---
title: Gestión de datos de archivos de Excel.
linktitle: Cells Datos
type: docs
weight: 110
url: /es/net/view-and-edit-excel-data/
description: Este artículo describe cómo ver y editar datos de archivos de Excel con la biblioteca Aspose.Cells.
---
{{% alert color="primary" %}}

 En[Acceso a Cells de una hoja de trabajo](/cells/es/net/accessing-cells-of-a-worksheet/), discutimos enfoques básicos para acceder a las celdas en una hoja de cálculo. Este artículo utiliza uno de esos enfoques para agregar diferentes tipos de datos a las celdas.

{{% /alert %}}

## **Agregando datos al Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

Aspose.Cells permite a los desarrolladores agregar datos a las celdas de las hojas de trabajo llamando al[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**poner valor**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) método. Aspose.Cells proporciona versiones sobrecargadas del[**poner valor**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) método que permite a los desarrolladores agregar diferentes tipos de datos a las celdas. Usando estas versiones sobrecargadas del[**poner valor**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)método, es posible agregar valores booleanos, de cadena, dobles, enteros o de fecha/hora, etc. a la celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Mejora de la eficiencia**

 Si utiliza[**poner valor**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)método para poner una gran cantidad de datos en una hoja de trabajo, debe agregar valores a las celdas, primero por filas y luego por columnas. Este enfoque mejora en gran medida la eficiencia de sus aplicaciones.

## **Recuperando datos de Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a las hojas de trabajo en el archivo. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Él[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)class proporciona varias propiedades que permiten a los desarrolladores recuperar valores de las celdas según sus tipos de datos. Estas propiedades incluyen:

- [**Valor de cadena**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): devuelve el valor de cadena de la celda.
- [**valor doble**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): devuelve el doble valor de la celda.
- [**valor bool**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): devuelve el valor booleano de la celda.
- [**Valor de fecha y hora**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): devuelve el valor de fecha/hora de la celda.
- [**valor flotante**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): devuelve el valor flotante de la celda.
- [**valorinterno**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)devuelve el valor entero de la celda.

 Cuando un campo no está lleno, las celdas con[**valor doble**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) o[**valor flotante**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)lanza una excepción.

 El tipo de datos contenidos en una celda también se puede verificar usando el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**Escribe**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) propiedad. De hecho, el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**Escribe**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) propiedad se basa en la[**Tipo de valor de celda**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)enumeración cuyos valores predefinidos se enumeran a continuación:

|**Cell Tipos de valor**|**Descripción**|
|:- |:- |
|esBool|Especifica que el valor de la celda es booleano.|
|esfechahora|Especifica que el valor de la celda es fecha/hora.|
|Es nulo|Representa una celda en blanco.|
|esnumérico|Especifica que el valor de la celda es numérico.|
|EsCadena|Especifica que el valor de la celda es una cadena.|
|Es desconocido|Especifica que el valor de la celda es desconocido.|

También puede usar los tipos de valores de celda predefinidos anteriores para comparar con el tipo de datos presente en cada celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Mientras trabajan en hojas de trabajo, los usuarios pueden agregar diferentes tipos de datos en las celdas. Estos tipos de datos pueden incluir valores booleanos, enteros, de coma flotante, de texto o de fecha/hora. Con Aspose.Cells, puede obtener los valores apropiados de las celdas según sus tipos de datos.

{{% /alert %}}

## **Temas avanzados**
- [Acceso a Cells de una hoja de trabajo](/cells/es/net/accessing-cells-of-a-worksheet/)
- [Convertir datos numéricos de texto en números](/cells/es/net/convert-text-numeric-data-to-number/)
- [Creación de subtotales](/cells/es/net/creating-subtotals/)
- [Filtrado de datos](/cells/es/net/data-filtering/)
- [Clasificación de datos](/cells/es/net/sort-data-of-excel/)
- [Validación de datos](/cells/es/net/data-validation/)
- [Exportar datos desde la hoja de trabajo](/cells/es/net/export-data-from-worksheet/)
- [Buscar o buscar datos](/cells/es/net/find-or-search-data/)
- [Obtenga el valor de cadena Cell con y sin formato](/cells/es/net/get-cell-string-value-with-and-without-formatting/)
- [Agregar HTML texto enriquecido dentro del Cell](/cells/es/net/adding-html-rich-text-inside-the-cell/)
- [Insertar hipervínculos en Excel u OpenOffice](/cells/es/net/insert-hyperlinks-to-excel/)
- [Importar datos a la hoja de trabajo](/cells/es/net/import-data-into-worksheet/)
- [Cómo y dónde usar enumeradores](/cells/es/net/how-and-where-to-use-enumerators/)
- [Mida el ancho y la altura del valor Cell en unidades de píxeles](/cells/es/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lectura de valores Cell en múltiples subprocesos simultáneamente](/cells/es/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversión entre nombre de celda e índice de fila/columna](/cells/es/net/names-and-indices/)
- [Complete los datos primero por fila y luego por columna](/cells/es/net/populate-data-first-by-row-then-by-column/)
- [Conservar el prefijo de comillas simples del valor o rango Cell](/cells/es/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Acceda y actualice las porciones de texto enriquecido de Cell](/cells/es/net/access-and-update-the-portions-of-rich-text-of-cell/)



