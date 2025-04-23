---
title: Encontrar el número máximo de filas y columnas admitidas por los formatos XLS y XLSX
type: docs
weight: 60
url: /es/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Escenarios de uso posibles**
Hay diferentes números de filas y columnas admitidos por los formatos de Excel. Por ejemplo, XLS admite 65536 filas y 256 columnas, mientras que XLSX admite 1048576 filas y 16384 columnas. Si deseas saber cuántas filas y columnas admite un formato determinado, puedes usar las propiedades [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) y [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn).
## **Encontrar el número máximo de filas y columnas admitidas por los formatos XLS y XLSX**
El siguiente código de ejemplo crea primero un libro de trabajo en formato XLS y luego en formato XLSX. Después de la creación, imprime los valores de [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) y [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn). Consulta la salida de la consola del código que se muestra a continuación para tu referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Salida de la consola

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
