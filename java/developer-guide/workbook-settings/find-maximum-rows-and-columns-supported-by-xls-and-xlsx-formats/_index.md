---
title: Find Maximum Rows and Columns supported by XLS and XLSX formats
type: docs
weight: 60
url: /java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Possible Usage Scenarios**
There are different number of rows and columns supported by Excel formats. For example, XLS supports 65536 rows and 256 columns while XLSX supports 1048576 rows and 16384 columns. If you want to know how many rows and columns are supported by given format, you can use [Workbook.Settings.MaxRow](https://apireference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) and [Workbook.Settings.MaxColumn](https://apireference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn) properties.
## **Find Maximum Rows and Columns supported by XLS and XLSX formats**
The following sample code creates workbook first in XLS and then in XLSX format. After creation, it prints the values of [Workbook.Settings.MaxRow](https://apireference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) and [Workbook.Settings.MaxColumn](https://apireference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn) properties. Please see the console output of the code given below for your reference.
## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Console Output

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
