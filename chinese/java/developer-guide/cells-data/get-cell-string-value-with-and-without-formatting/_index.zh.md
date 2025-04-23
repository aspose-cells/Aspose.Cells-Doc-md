---
title: 获取带格式和不带格式的单元格字符串值
type: docs
weight: 230
url: /zh/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells提供了[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-)方法，可用来获取单元格的字符串值，无论是否带格式。例如，假设你有一个值为0.012345的单元格，并将其格式化为只显示两位小数，那么在Excel中显示为0.01。你可以用[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-)方法同时以0.01和0.012345的形式获取字符串值。此方法接受[CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)枚举作为参数，枚举值如下：

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **获取有格式和无格式的单元格字符串值**
以下示例代码演示了[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-)方法的用法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **控制台输出**
以下是上面示例代码的控制台输出。

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
