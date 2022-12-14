---
title: Encuentre filas y columnas máximas compatibles con los formatos XLS y XLSX
type: docs
weight: 60
url: /es/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Posibles escenarios de uso**
Hay diferentes números de filas y columnas compatibles con los formatos de Excel. Por ejemplo, XLS admite 65536 filas y 256 columnas, mientras que XLSX admite 1048576 filas y 16384 columnas. Si desea saber cuántas filas y columnas admite un formato determinado, puede utilizar[Libro de trabajo.Configuración.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)y[Libro de trabajo.Configuración.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)propiedades.
## **Encuentre filas y columnas máximas compatibles con los formatos XLS y XLSX**
El siguiente código de ejemplo crea un libro de trabajo primero en formato XLS y luego en formato XLSX. Después de la creación, imprime los valores de[Libro de trabajo.Configuración.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)y[Libro de trabajo.Configuración.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)propiedades. Consulte la salida de la consola del código que se proporciona a continuación para su referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Salida de consola

{{< highlight "java" >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
