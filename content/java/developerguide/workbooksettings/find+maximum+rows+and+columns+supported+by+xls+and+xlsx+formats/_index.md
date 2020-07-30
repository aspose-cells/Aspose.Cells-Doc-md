---
title : "Find Maximum Rows and Columns supported by XLS and XLSX formats" 
description : "" 
weight : 12120 
toc : false
type: docs
url: /java/developerguide/workbooksettings/find+maximum+rows+and+columns+supported+by+xls+and+xlsx+formats/
---

# Aspose.Cells for Java : Find Maximum Rows and Columns supported by XLS and XLSX formats


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Find Maximum Rows and Columns supported by XLS and XLSX formats](#find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

There are different number of rows and columns supported by Excel formats. For example, XLS supports 65536 rows and 256 columns while XLSX supports 1048576 rows and 16384 columns. If you want to know how many rows and columns are supported by given format, you can use [Workbook.Settings.MaxRow](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#MaxRow) and [Workbook.Settings.MaxColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#MaxColumn) properties.

## Find Maximum Rows and Columns supported by XLS and XLSX formats

The following sample code creates workbook first in XLS and then in XLSX format. After creation, it prints the values of [Workbook.Settings.MaxRow](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#MaxRow) and [Workbook.Settings.MaxColumn](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#MaxColumn) properties. Please see the console output of the code given below for your reference.

## Sample Code

Console Output

{{< code lang="cs" >}}
Maximum Rows and Columns supported by XLS format.
Maximum Rows: 65536
Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.
Maximum Rows: 1048576
Maximum Columns: 16384
{{< /code >}}

