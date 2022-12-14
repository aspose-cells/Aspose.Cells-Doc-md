---
title: Encuentre filas y columnas máximas compatibles con los formatos XLS y XLSX
type: docs
weight: 20
url: /es/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Posibles escenarios de uso**

Hay diferentes números de filas y columnas compatibles con los formatos de Excel. Por ejemplo, XLS admite 65536 filas y 256 columnas, mientras que XLSX admite 1048576 filas y 16384 columnas. Si desea saber cuántas filas y columnas admite un formato determinado, puede utilizar[**Libro de trabajo.Configuración.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) y[**Libro de trabajo.Configuración.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)propiedades.

## **Encuentre filas y columnas máximas compatibles con los formatos XLS y XLSX**

El siguiente código de ejemplo crea un libro de trabajo primero en formato XLS y luego en formato XLSX. Después de la creación, imprime los valores de[**Libro de trabajo.Configuración.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) y[**Libro de trabajo.Configuración.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)propiedades. Consulte la salida de la consola del código que se proporciona a continuación para su referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
