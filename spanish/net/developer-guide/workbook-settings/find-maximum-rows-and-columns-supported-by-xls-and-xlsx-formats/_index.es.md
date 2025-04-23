---
title: Encontrar el número máximo de filas y columnas admitidas por los formatos XLS y XLSX
type: docs
weight: 20
url: /es/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Escenarios de uso posibles**

Existen diferentes números de filas y columnas admitidos por los formatos de Excel. Por ejemplo, XLS admite 65536 filas y 256 columnas mientras que XLSX admite 1048576 filas y 16384 columnas. Si deseas saber cuántas filas y columnas son admitidas por un formato dado, puedes utilizar las propiedades [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) y [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn).

## **Encontrar el número máximo de filas y columnas admitidas por los formatos XLS y XLSX**

El siguiente código de muestra crea primero un libro de trabajo en formato XLS y luego en formato XLSX. Después de la creación, imprime los valores de las propiedades [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) y [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn). Por favor, consulta la salida de consola del código que se muestra a continuación para tu referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
