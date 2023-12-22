---
title: Autoajustar filas y columnas
type: docs
weight: 20
url: /es/net/autofit-rows-and-columns/
description: Este artículo muestra cómo ajustar automáticamente filas, columnas, filas de celdas combinadas y filas en un rango de celdas mediante Aspose.Cells for .NET API.
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios ajustar automáticamente el ancho y el alto de las celdas según su contenido. Esta función también está disponible a través de Aspose.Cells para que los desarrolladores puedan dimensionar automáticamente las dimensiones de una celda en tiempo de ejecución.

{{% /alert %}}

##  **Montaje automático**

Aspose.Cells proporciona un[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de cálculo en un archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de trabajo. Este artículo analiza el uso de[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase para ajustar automáticamente filas o columnas.

###  **Fila de ajuste automático: sencilla**

 El enfoque más sencillo para ajustar automáticamente el tamaño del ancho y alto de una fila es llamar al[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**AutoAjustarFila**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) método. El[**AutoAjustarFila**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)El método toma un índice de fila (de la fila cuyo tamaño se va a cambiar) como parámetro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **Cómo ajustar automáticamente la fila en un rango de Cells**

 Una fila se compone de muchas columnas. Aspose.Cells permite a los desarrolladores ajustar automáticamente una fila según el contenido de un rango de celdas dentro de la fila llamando a una versión sobrecargada del[**AutoAjustarFila**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)método. Toma los siguientes parámetros:

- *Índice de fila**, el índice de la fila que se va a ajustar automáticamente.
- *Índice de la primera columna**, el índice de la primera columna de la fila.
- *Índice de la última columna**, el índice de la última columna de la fila.

 El[**AutoAjustarFila**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)El método verifica el contenido de todas las columnas de la fila y luego ajusta automáticamente la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **Cómo ajustar automáticamente la columna en un rango de Cells**

 Una columna se compone de muchas filas. Es posible ajustar automáticamente una columna según el contenido de un rango de celdas de la columna llamando a una versión sobrecargada de[**Columna de ajuste automático**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)método que toma los siguientes parámetros:

- *Índice de columna**, el índice de la columna que se va a ajustar automáticamente.
- *Índice de la primera fila**, el índice de la primera fila de la columna.
- *Índice de la última fila**, el índice de la última fila de la columna.

 El[**Columna de ajuste automático**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)El método verifica el contenido de todas las filas de la columna y luego ajusta automáticamente la columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **Cómo ajustar automáticamente filas para Cells combinado**

 Con Aspose.Cells es posible ajustar automáticamente filas incluso para celdas que se han fusionado utilizando el[**Opciones de AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**Opciones de AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)la clase proporciona[**Tipo de celdas fusionadas de ajuste automático**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) propiedad que se puede utilizar para ajustar automáticamente las filas de las celdas fusionadas.[**Tipo de celdas fusionadas de ajuste automático**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)acepta[**Tipo de celdas fusionadas de ajuste automático**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) enumerable que tiene los siguientes miembros.

- Ninguno: ignora las celdas combinadas.
- FirstLine: solo expande la altura de la primera fila.
- LastLine: solo expande la altura de la última fila.
- EachLine: solo expande la altura de cada fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 También puede intentar utilizar las versiones sobrecargadas de[**AutoAjustarFilas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**AutoAjustarColumnas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) métodos que aceptan un rango de filas/columnas y una instancia de[**Opciones de AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) para ajustar automáticamente las filas/columnas seleccionadas con su deseado[**Opciones de AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)respectivamente.

Las firmas de los métodos antes mencionados son las siguientes:

1.  AutoFitRows(int startRow, int endRow,[**Opciones de AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)opciones)
1.  AutoFitColumns(int primeracolumna, int últimacolumna,[**Opciones de AutoFitter**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)opciones)

{{% /alert %}}

##  **Importante saber**

{{% alert color="primary" %}}

Si se fusiona una celda, no se aplicarán los métodos de Autoajuste, que es el mismo comportamiento que en Microsoft Excel. Puede solucionar esto utilizando el filtro automático API. Además, si el texto de una celda está ajustado, el[**Columna de ajuste automático**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) El método tampoco se aplicará. Otra cosa que debes saber es que el*Ajuste automático*Los métodos requieren mucho tiempo. Por lo tanto, debes llamar a estos métodos lo menos posible para garantizar la eficiencia de tu aplicación.

{{% /alert %}}

##  **Temas avanzados**
- [AutoFit filas para fusionado Cells](/cells/es/net/autofit-rows-for-merged-cells/)
