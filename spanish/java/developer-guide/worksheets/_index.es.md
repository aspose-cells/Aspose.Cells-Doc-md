---
title: Administrar hojas de trabajo
linktitle: Hojas de trabajo
type: docs
weight: 60
url: /es/java/manage-worksheets/
---
{{% alert color="primary" %}}

Los desarrolladores pueden crear y administrar fácilmente hojas de trabajo en sus archivos de Excel mediante programación usando el API flexible de Aspose.Cells. En este tema, discutiremos algunos enfoques para agregar y quitar hojas de trabajo en archivos de Excel.

{{% /alert %}}

Administrar hojas de trabajo usando Aspose.Cells es tan fácil como ABC. En esta sección, describiremos cómo podemos:

1. Cree un nuevo archivo de Excel desde cero y agréguele una hoja de trabajo
1. Agregar hojas de trabajo a las hojas de cálculo del diseñador
1. Acceder a las hojas de trabajo usando el nombre de la hoja
1. Eliminar una hoja de trabajo de un archivo de Excel usando su nombre de hoja
1. Eliminar una hoja de trabajo de un archivo de Excel usando su índice de hoja

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel.[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Veamos cómo podemos hacer uso de este conjunto básico de API.

## **Agregar hojas de trabajo a un nuevo archivo de Excel**

 Para crear un nuevo archivo de Excel mediante programación, los desarrolladores tendrían que crear un objeto de[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase que representa un archivo de Excel. Entonces los desarrolladores pueden llamar[**agregar**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) método de la[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . cuando llamamos[**agregar**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ), se agrega automáticamente una hoja de cálculo vacía al archivo de Excel, a la que se puede hacer referencia pasando el índice de hoja de la hoja de cálculo recién agregada al[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Una vez que se obtiene la referencia de la hoja de trabajo, los desarrolladores pueden trabajar en sus hojas de trabajo de acuerdo con sus requisitos. Una vez que se realiza el trabajo en las hojas de trabajo, los desarrolladores pueden guardar su archivo de Excel recién creado con nuevas hojas de trabajo llamando al[**ahorrar**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) método de la[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)clase.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Adición de hojas de trabajo a una hoja de cálculo de Designer**

El proceso de agregar hojas de trabajo a una hoja de cálculo de diseñador es completamente igual al del enfoque anterior, excepto que el archivo de Excel ya está creado y debemos abrir ese archivo de Excel primero antes de agregarle una hoja de trabajo. Se puede abrir una hoja de cálculo de diseñador pasando la ruta del archivo o la secuencia mientras se inicializa el[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)clase.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Acceder a las hojas de trabajo usando el nombre de la hoja**

Los desarrolladores pueden acceder u obtener cualquier hoja de trabajo especificando su nombre o índice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Eliminación de hojas de trabajo usando el nombre de la hoja**

 A veces, los desarrolladores pueden necesitar eliminar hojas de trabajo de archivos de Excel existentes y esa tarea se puede realizar llamando al[**eliminar en**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) método de la[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) recopilación. Podemos pasar el nombre de la hoja al[**eliminar en**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) método para eliminar una hoja de trabajo específica.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Eliminación de hojas de cálculo mediante el índice de hojas**

El enfoque anterior de eliminar hojas de trabajo funciona bien si los desarrolladores ya conocen los nombres de las hojas de trabajo que se eliminarán. Pero, ¿qué sucede si no conoce el nombre de la hoja de trabajo que desea eliminar de su archivo de Excel?

 Bueno, en tales circunstancias, los desarrolladores pueden usar una versión sobrecargada de[**eliminar en**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)método que toma el índice de hoja de la hoja de trabajo en lugar de su nombre de hoja.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Temas avanzados**
- [Activación de hojas y activación de un Cell en la hoja de trabajo](/cells/es/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Copiar y mover hojas de trabajo dentro y entre libros de trabajo](/cells/es/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Copiar y mover hojas de trabajo](/cells/es/java/copying-and-moving-worksheets/)
- [Cuente el número de celdas en la hoja de trabajo](/cells/es/java/count-number-of-cells-in-the-worksheet/)
- [Detectar hojas de trabajo vacías](/cells/es/java/detecting-empty-worksheets/)
- [Averigüe si la hoja de trabajo es una hoja de diálogo](/cells/es/java/find-if-the-worksheet-is-dialog-sheet/)
- [Obtener identificación única de la hoja de trabajo](/cells/es/java/get-worksheet-unique-id/)
- [Insertar imagen de fondo en Excel](/cells/es/java/insert-background-image-to-excel/)
- [Crear, manipular o eliminar escenarios de las hojas de trabajo](/cells/es/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestión de saltos de página](/cells/es/java/managing-page-breaks/)
- [Funciones de configuración de página](/cells/es/java/page-setup-features/)
- [Actualice referencias en otras hojas de trabajo mientras elimina columnas y filas en blanco en una hoja de trabajo](/cells/es/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Utilice la propiedad Sheet.SheetId de OpenXml usando Aspose.Cells](/cells/es/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Trabajar con fondo en archivos ODS](/cells/es/java/working-with-background-in-ods-files/)
- [Vistas de la hoja de cálculo](/cells/es/java/worksheet-views/)
