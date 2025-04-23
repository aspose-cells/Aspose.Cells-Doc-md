---
title: Administrar hojas de cálculo de archivos de Microsoft Excel
linktitle: Hojas de cálculo
type: docs
weight: 90
url: /es/net/manage-worksheets/
description: Agregar hojas de cálculo, eliminar hojas de cálculo y hoja activa utilizando Aspose.Cells.
---


{{% alert color="primary" %}}

Los desarrolladores pueden crear y administrar fácilmente hojas de cálculo en archivos de Microsoft Excel programáticamente utilizando la API flexible de Aspose.Cells. Este tema describe los enfoques para agregar y eliminar hojas de cálculo en archivos de Microsoft Excel.

{{% /alert %}}

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para administrar las hojas de cálculo.

## **Añadir hojas de cálculo a un nuevo archivo de Excel**

Para crear un nuevo archivo de Excel programáticamente:

1. Cree un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Llame al método [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) de la clase [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). Se añade automáticamente una hoja de cálculo vacía al archivo de Excel. Se puede hacer referencia a ella pasando el índice de hoja de la nueva hoja de cálculo a la colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets).
1. Obtenga una referencia de la hoja de cálculo.
1. Realice el trabajo en las hojas de cálculo.
1. Guarde el nuevo archivo de Excel con las nuevas hojas de cálculo llamando al método [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Añadir hojas de cálculo a una hoja de cálculo de diseñador**

El proceso de agregar hojas de cálculo a una hoja de cálculo predefinida es igual al de agregar una nueva hoja de cálculo, excepto que el archivo de Excel ya existe, por lo que debe abrirse antes de que se agreguen las hojas de cálculo. Una hoja de cálculo predefinida puede ser abierta por la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Acceso a las hojas de cálculo usando el nombre de la hoja**

Acceda a cualquier hoja de cálculo especificando su nombre o índice

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Eliminar hojas de cálculo utilizando el nombre de la hoja**

Para eliminar hojas de cálculo de un archivo, llame al método [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) de la clase [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). Pase el nombre de la hoja al método [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) para eliminar una hoja de cálculo específica

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Eliminar hojas de cálculo utilizando el índice de la hoja**

Eliminar hojas de cálculo por nombre funciona bien cuando se conoce el nombre de la hoja de cálculo. Si no conoce el nombre de la hoja de cálculo, use una versión sobrecargada del método [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) que tome el índice de la hoja de cálculo en lugar de su nombre de hoja

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Activar hojas y hacer que una celda sea activa en la hoja de cálculo**

A veces, necesita que una hoja de cálculo específica esté activa y visible cuando un usuario abre un archivo de Microsoft Excel en Excel. De manera similar, es posible que desee activar una celda específica y establecer las barras de desplazamiento para mostrar la celda activa
Aspose.Cells es capaz de realizar todas estas tareas

Una **hoja activa** es una hoja en la que está trabajando: el nombre de la hoja activa en la pestaña aparece en negrita de forma predeterminada

Una **celda activa** es una celda seleccionada, la celda en la que se ingresa datos cuando comienza a escribir. Solo una celda está activa a la vez. La celda activa se resalta con un borde grueso

### **Activar hojas y hacer que una celda sea activa**

Aspose.Cells proporciona llamadas específicas de API para activar una hoja y una celda. Por ejemplo, la propiedad [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) es útil para establecer la hoja activa en un libro de trabajo
De manera similar, la propiedad [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) se usa para establecer y obtener una celda activa en la hoja de cálculo

Para asegurarse de que las barras de desplazamiento horizontal o vertical estén en la posición del índice de fila y columna que desea mostrar datos específicos, use las propiedades [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) y [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)

El siguiente ejemplo muestra cómo activar una hoja de cálculo y hacer que una celda sea activa en ella. En la salida generada, las barras de desplazamiento se desplazarán para que la segunda fila y la segunda columna sean su primera fila y columna visibles

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Temas avanzados**
- [Copiar y mover hojas de cálculo](/cells/es/net/copying-and-moving-worksheets/)
- [Contar el número de celdas en la hoja de cálculo](/cells/es/net/count-number-of-cells-in-the-worksheet/)
- [Detectar hojas de cálculo vacías](/cells/es/net/detecting-empty-worksheets/)
- [Buscar si la hoja de trabajo es una hoja de diálogo](/cells/es/net/find-if-the-worksheet-is-dialog-sheet/)
- [Obtener el ID único de la hoja de trabajo](/cells/es/net/get-worksheet-unique-id/)
- [Crear, manipular o eliminar escenarios de hojas de trabajo](/cells/es/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestionar saltos de página](/cells/es/net/managing-page-breaks/)
- [Funciones de configuración de página](/cells/es/net/page-setup-features/)
- [Imprimir múltiples copias de una hoja de trabajo](/cells/es/net/print-multiple-copies-of-a-worksheet/)
- [Utilizar la propiedad SheetId de OpenXml usando Aspose.Cells](/cells/es/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Vistas de hojas de trabajo](/cells/es/net/worksheet-views/)

{{< app/cells/assistant language="csharp" >}}
