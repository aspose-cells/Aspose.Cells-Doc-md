---
title: 查找XLS和XLSX格式支持的最大行数和列数
type: docs
weight: 20
url: /zh/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **可能的使用场景**

Excel格式支持不同数量的行和列。例如，XLS支持65536行和256列，而XLSX支持1048576行和16384列。如果要了解给定格式支持的行数和列数，可以使用[**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow)和[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)属性。

## **查找XLS和XLSX格式支持的最大行数和列数**

以下示例代码首先创建XLS和XLSX格式的工作簿。创建后，它将打印[**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow)和[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)属性的值。请查看下面给出的代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **控制台输出**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
