---
title: Find Maximum Rows and Columns supported by XLS and XLSX formats
type: docs
weight: 20
url: /net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Possible Usage Scenarios**

There are different number of rows and columns supported by Excel formats. For example, XLS supports 65536 rows and 256 columns while XLSX supports 1048576 rows and 16384 columns. If you want to know how many rows and columns are supported by given format, you can use [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) and [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn) properties.

## **Find Maximum Rows and Columns supported by XLS and XLSX formats**

The following sample code creates workbook first in XLS and then in XLSX format. After creation, it prints the values of [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) and [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn) properties. Please see the console output of the code given below for your reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Console Output**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}