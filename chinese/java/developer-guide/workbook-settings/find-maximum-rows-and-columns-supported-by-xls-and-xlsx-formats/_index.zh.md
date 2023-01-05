---
title: 查找 XLS 和 XLSX 格式支持的最大行数和列数
type: docs
weight: 60
url: /zh/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **可能的使用场景**
Excel 格式支持的行数和列数不同。例如，XLS 支持 65536 行和 256 列，而 XLSX 支持 1048576 行和 16384 列。如果您想知道给定格式支持多少行和列，您可以使用[工作簿.设置.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)和[工作簿.设置.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)特性。
## **查找 XLS 和 XLSX 格式支持的最大行数和列数**
以下示例代码首先以 XLS 格式创建工作簿，然后以 XLSX 格式创建工作簿。创建后，它打印值[工作簿.设置.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)和[工作簿.设置.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)特性。请查看下面给出的代码的控制台输出以供参考。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

控制台输出

{{< highlight "java" >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
