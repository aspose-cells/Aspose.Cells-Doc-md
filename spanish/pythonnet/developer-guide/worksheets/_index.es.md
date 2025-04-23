---
title: Administrar hojas de cálculo de archivos de Microsoft Excel
linktitle: Hojas de cálculo
type: docs
weight: 90
url: /es/python-net/manage-worksheets/
description: Este artículo muestra cómo gestionar las hojas de cálculo de los archivos de Microsoft Excel mediante la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Gestionar hojas de cálculo de archivos de Microsoft Excel en Python, Agregar hoja de cálculo en Python, Quitar hoja de cálculo en Python, Cómo agregar hojas de cálculo a un nuevo archivo de Excel en Python, Cómo agregar hojas de cálculo a una hoja de cálculo prediseñada en Python, Cómo acceder a hojas de cálculo mediante el nombre de la hoja en Python, Cómo eliminar hojas de cálculo mediante el nombre de la hoja en Python, Cómo eliminar hojas de cálculo mediante el índice de la hoja en Python, Cómo activar hojas y hacer que una celda esté activa en Python.
---


{{% alert color="primary" %}}

Los desarrolladores pueden crear y administrar fácilmente hojas de cálculo en archivos de Microsoft Excel programáticamente utilizando la API flexible de Aspose.Cells. Este tema describe los enfoques para agregar y eliminar hojas de cálculo en archivos de Microsoft Excel.

{{% /alert %}}

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para administrar las hojas de cálculo.

## **Cómo agregar hojas de cálculo a un nuevo archivo de Excel**

Para crear un nuevo archivo de Excel programáticamente:

1. Cree un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Llame al método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) de la clase [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). Se añade automáticamente una hoja de cálculo vacía al archivo de Excel. Se puede hacer referencia a ella pasando el índice de hoja de la nueva hoja de cálculo a la colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/).
1. Obtenga una referencia de la hoja de cálculo.
1. Realice el trabajo en las hojas de cálculo.
1. Guarde el nuevo archivo de Excel con las nuevas hojas de cálculo llamando al método [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **Cómo agregar hojas de cálculo a una hoja de cálculo prediseñada**

El proceso de agregar hojas de cálculo a una hoja de cálculo predefinida es igual al de agregar una nueva hoja de cálculo, excepto que el archivo de Excel ya existe, por lo que debe abrirse antes de que se agreguen las hojas de cálculo. Una hoja de cálculo predefinida puede ser abierta por la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **Cómo acceder a hojas de cálculo mediante el nombre de la hoja**

Acceda a cualquier hoja de cálculo especificando su nombre o índice

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **Cómo eliminar hojas de cálculo mediante el nombre de la hoja**

Para eliminar hojas de cálculo de un archivo, llame al método [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) de la clase [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). Pase el nombre de la hoja al método [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) para eliminar una hoja de cálculo específica

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **Cómo eliminar hojas de cálculo mediante el índice de la hoja**

Eliminar hojas de cálculo por nombre funciona bien cuando se conoce el nombre de la hoja de cálculo. Si no conoce el nombre de la hoja de cálculo, utilice el método [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int) que toma el índice de la hoja de cálculo en lugar de su nombre.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **Cómo activar hojas y hacer que una celda esté activa en la hoja de cálculo**

A veces, necesita que una hoja de cálculo específica esté activa y visible cuando un usuario abre un archivo de Microsoft Excel en Excel. De manera similar, es posible que desee activar una celda específica y establecer las barras de desplazamiento para mostrar la celda activa
Aspose.Cells es capaz de realizar todas estas tareas

Una **hoja activa** es una hoja en la que está trabajando: el nombre de la hoja activa en la pestaña aparece en negrita de forma predeterminada

Una **celda activa** es una celda seleccionada, la celda en la que se ingresa datos cuando comienza a escribir. Solo una celda está activa a la vez. La celda activa se resalta con un borde grueso

### **Cómo activar hojas y hacer que una celda esté activa**

Aspose.Cells proporciona llamadas específicas de API para activar una hoja y una celda. Por ejemplo, la propiedad [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) es útil para establecer la hoja activa en un libro de trabajo
De manera similar, la propiedad [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) se usa para establecer y obtener una celda activa en la hoja de cálculo

Para asegurarse de que las barras de desplazamiento horizontal o vertical estén en la posición del índice de fila y columna que desea mostrar datos específicos, use las propiedades [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) y [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/)

El siguiente ejemplo muestra cómo activar una hoja de cálculo y hacer que una celda sea activa en ella. En la salida generada, las barras de desplazamiento se desplazarán para que la segunda fila y la segunda columna sean su primera fila y columna visibles

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

