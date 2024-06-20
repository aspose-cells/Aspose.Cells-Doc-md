---
title: Gestionar hojas de cálculo
linktitle: Hojas de cálculo
type: docs
weight: 60
url: /es/java/manage-worksheets/
---

{{% alert color="primary" %}}

Los desarrolladores pueden crear y gestionar hojas de cálculo en sus archivos de Excel de forma programática utilizando la API flexible de Aspose.Cells. En este tema, discutiremos algunos enfoques para añadir y eliminar hojas de cálculo en archivos de Excel.

{{% /alert %}}

Gestionar hojas de cálculo con Aspose.Cells es tan fácil como el ABC. En esta sección, describiremos cómo podemos:

1. Crear un nuevo archivo de Excel desde cero y añadir una hoja de cálculo a él
1. Añadir hojas de cálculo a hojas de cálculo diseñadas
1. Acceder a las hojas de cálculo usando el nombre de la hoja
1. Eliminar una hoja de cálculo de un archivo de Excel usando su nombre de la hoja
1. Eliminar una hoja de cálculo de un archivo de Excel usando su índice de hoja

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Veamos cómo podemos hacer uso de este conjunto básico de APIs.

## **Añadir hojas de cálculo a un nuevo archivo de Excel**

Para crear un nuevo archivo de Excel programáticamente, los desarrolladores necesitarían crear un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel. Luego, los desarrolladores pueden llamar al método [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) de la [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Cuando llamamos al método [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--), se agrega automáticamente una hoja de cálculo vacía al archivo de Excel, la cual puede ser referenciada pasando el índice de la hoja recién agregada a la [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Después de obtener la referencia de la hoja de cálculo, los desarrolladores pueden trabajar en sus hojas de cálculo según sus requisitos. Después de completar el trabajo en las hojas de cálculo, los desarrolladores pueden guardar su archivo de Excel recién creado con nuevas hojas de cálculo llamando al método [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Añadir hojas de cálculo a una hoja de cálculo de diseñador**

El proceso de agregar hojas de cálculo a una hoja de cálculo de diseño es completamente igual al enfoque anterior, excepto que el archivo de Excel ya está creado y necesitamos abrir ese archivo de Excel primero antes de agregar una hoja de cálculo a él. Una hoja de cálculo de diseño puede ser abierta pasando la ruta del archivo o el flujo al inicializar la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Acceso a las hojas de cálculo usando el nombre de la hoja**

Los desarrolladores pueden acceder o obtener cualquier hoja de cálculo especificando su nombre o índice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Eliminar hojas de cálculo utilizando el nombre de la hoja**

A veces, los desarrolladores pueden necesitar eliminar hojas de cálculo de archivos de Excel existentes y esa tarea se puede realizar llamando al método [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) de la colección [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Podemos pasar el nombre de la hoja al método [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) para eliminar una hoja de cálculo específica.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Eliminar hojas de cálculo utilizando el índice de la hoja**

El enfoque anterior de eliminar hojas de cálculo funciona bien si los desarrolladores ya conocen los nombres de las hojas de cálculo que se van a eliminar. Pero, ¿qué pasa si no conoces el nombre de la hoja de cálculo que deseas eliminar de tu archivo de Excel?

Bueno, en tales circunstancias, los desarrolladores pueden usar una versión sobrecargada del método [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)) que toma el índice de la hoja de cálculo en lugar de su nombre de hoja.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Temas avanzados**
- [Activar Hojas y Activar una Celda en la Hoja de Cálculo](/cells/es/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Copiar y Mover Hojas de Cálculo Dentro y Entre Libros de Trabajo](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Copiar y mover hojas de cálculo](/cells/es/java/copying-and-moving-worksheets/)
- [Contar el número de celdas en la hoja de cálculo](/cells/es/java/count-number-of-cells-in-the-worksheet/)
- [Detectar hojas de cálculo vacías](/cells/es/java/detecting-empty-worksheets/)
- [Buscar si la hoja de trabajo es una hoja de diálogo](/cells/es/java/find-if-the-worksheet-is-dialog-sheet/)
- [Obtener el ID único de la hoja de trabajo](/cells/es/java/get-worksheet-unique-id/)
- [Insertar imagen de fondo en Excel](/cells/es/java/insert-background-image-to-excel/)
- [Crear, manipular o eliminar escenarios de hojas de trabajo](/cells/es/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestionar saltos de página](/cells/es/java/managing-page-breaks/)
- [Funciones de configuración de página](/cells/es/java/page-setup-features/)
- [Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo](/cells/es/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Utilizar la propiedad SheetId de OpenXml usando Aspose.Cells](/cells/es/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Trabajar con fondo en archivos ODS](/cells/es/java/working-with-background-in-ods-files/)
- [Vistas de hojas de trabajo](/cells/es/java/worksheet-views/)
