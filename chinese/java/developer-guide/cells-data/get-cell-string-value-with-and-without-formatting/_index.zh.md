---
title: 获取带格式和不带格式的单元格字符串值
type: docs
weight: 230
url: /zh/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells提供了一种方法[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\))，可用于获取具有或不具有任何格式的单元格的字符串值。例如，如果单元格的值为0.012345，并且已将其格式化为仅显示两位小数，那么在Excel中将显示为0.01。您可以使用[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\))方法检索0.01和0.012345这两种字符串值。它将[CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)枚举作为参数，其具有以下值

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **获取有格式和无格式的单元格字符串值**
以下示例代码解释了如何使用 [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **控制台输出**
以下是上面示例代码的控制台输出。

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
