---
title: Administre hojas de trabajo de Microsoft archivos de Excel.
linktitle: Hojas de trabajo
type: docs
weight: 90
url: /es/net/manage-worksheets/
description: Agregue la hoja de trabajo, elimine la hoja de trabajo y la hoja activa usando Aspose.Cells.
---
{{% alert color="primary" %}}

Los desarrolladores pueden crear y administrar fácilmente hojas de trabajo en archivos Microsoft de Excel mediante programación usando Aspose.Cells' flexible API. Este tema describe enfoques para agregar y eliminar hojas de trabajo en archivos Microsoft de Excel.

{{% /alert %}}

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo.

## **Agregar hojas de trabajo a un nuevo archivo de Excel**

Para crear un nuevo archivo de Excel mediante programación:

1.  Crea un objeto de la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase.
1.  Llama a[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) metodo de la[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) clase. Una hoja de cálculo vacía se agrega automáticamente al archivo de Excel. Se puede hacer referencia al pasar el índice de la hoja de la nueva hoja de trabajo al[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) recopilación.
1. Obtenga una referencia de la hoja de trabajo.
1. Realizar el trabajo en las hojas de trabajo.
1.  Guarde el nuevo archivo de Excel con nuevas hojas de trabajo llamando al[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase'[**Ahorrar**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Adición de hojas de trabajo a una hoja de cálculo de Designer**

 El proceso de agregar hojas de trabajo a una hoja de cálculo de diseñador es el mismo que el de agregar una nueva hoja de trabajo, excepto que el archivo de Excel ya existe, por lo que debe abrirse antes de agregar las hojas de trabajo. Una hoja de cálculo de diseñador puede ser abierta por el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Acceder a las hojas de trabajo usando el nombre de la hoja**

Acceda a cualquier hoja de trabajo especificando su nombre o índice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Eliminación de hojas de trabajo usando el nombre de la hoja**

Para eliminar hojas de trabajo de un archivo, llame al[**Eliminar en**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) método de[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) clase. Pase el nombre de la hoja al[**Eliminar en**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)método para eliminar una hoja de trabajo específica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Eliminación de hojas de cálculo mediante el índice de hojas**

 La eliminación de hojas de trabajo por nombre funciona bien cuando se conoce el nombre de la hoja de trabajo. Si no conoce el nombre de la hoja de cálculo, utilice una versión sobrecargada de la[**Eliminar en**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)método que toma el índice de hoja de la hoja de trabajo en lugar de su nombre de hoja.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Activar hojas y hacer un activo Cell en la hoja de trabajo**

A veces, necesita que una hoja de trabajo específica esté activa y se muestre cuando un usuario abre un archivo de Excel Microsoft en Excel. De manera similar, es posible que desee activar una celda específica y configurar las barras de desplazamiento para mostrar la celda activa.
Aspose.Cells es capaz de hacer todas estas tareas.

 Un**hoja activa** es una hoja en la que está trabajando: el nombre de la hoja activa en la pestaña está en negrita de forma predeterminada.

 Un**Célula activa** es una celda seleccionada, la celda en la que se ingresan los datos cuando comienza a escribir. Solo una celda está activa a la vez. La celda activa está resaltada por un borde grueso.

### **Activando Hojas y Haciendo un Cell Activo**

Aspose.Cells proporciona llamadas API específicas para activar una hoja y una celda. Por ejemplo, el[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)La propiedad es útil para configurar la hoja activa en un libro de trabajo.
Similarmente,[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)La propiedad se utiliza para establecer y obtener una celda activa en la hoja de cálculo.

Para asegurarse de que las barras de desplazamiento horizontal o vertical estén en la posición del índice de fila y columna en la que desea mostrar datos específicos, use el[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) y[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)propiedades.

El siguiente ejemplo muestra cómo activar una hoja de trabajo y hacer una celda activa en ella. En la salida generada, las barras de desplazamiento se desplazarán para hacer que la segunda fila y la segunda columna sean sus primeras filas y columnas visibles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Temas avanzados**
- [Copiar y mover hojas de trabajo](/cells/es/net/copying-and-moving-worksheets/)
- [Cuente el número de celdas en la hoja de trabajo](/cells/es/net/count-number-of-cells-in-the-worksheet/)
- [Detectar hojas de trabajo vacías](/cells/es/net/detecting-empty-worksheets/)
- [Averigüe si la hoja de trabajo es una hoja de diálogo](/cells/es/net/find-if-the-worksheet-is-dialog-sheet/)
- [Obtener identificación única de la hoja de trabajo](/cells/es/net/get-worksheet-unique-id/)
- [Crear, manipular o eliminar escenarios de las hojas de trabajo](/cells/es/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestión de saltos de página](/cells/es/net/managing-page-breaks/)
- [Funciones de configuración de página](/cells/es/net/page-setup-features/)
- [Imprimir varias copias de una hoja de trabajo](/cells/es/net/print-multiple-copies-of-a-worksheet/)
- [Utilice la propiedad Sheet.SheetId de OpenXml usando Aspose.Cells](/cells/es/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Vistas de la hoja de cálculo](/cells/es/net/worksheet-views/)

