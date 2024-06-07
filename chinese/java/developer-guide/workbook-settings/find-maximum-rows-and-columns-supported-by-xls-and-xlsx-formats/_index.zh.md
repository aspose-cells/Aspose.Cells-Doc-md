---
title: 查找XLS和XLSX格式支持的最大行数和列数
type: docs
weight: 60
url: /zh/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **可能的使用场景**
不同的Excel格式支持不同数量的行和列。例如，XLS支持65536行和256列，而XLSX支持1048576行和16384列。如果您想知道给定格式支持多少行和列，可以使用[Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)和[Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)属性。
## **查找XLS和XLSX格式支持的最大行数和列数**
以下示例代码首先以XLS格式创建工作簿，然后以XLSX格式创建工作簿。创建后，打印[Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)和[Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)属性的值。请参考下方给出的代码输出控制台输出。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

控制台输出

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
