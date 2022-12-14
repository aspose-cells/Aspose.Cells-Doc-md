---
title: 获取 Cell 带格式和不带格式的字符串值
type: docs
weight: 230
url: /zh/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells提供方法[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) 可用于获取带或不带任何格式的单元格的字符串值。假设您有一个值为 0.012345 的单元格，并且您已将其格式化为仅显示两位小数。然后它将在 Excel 中显示为 0.01。您可以使用 0.01 和 0.012345 检索字符串值[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)） 方法。它需要[CellValueFormat策略](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)枚举作为具有以下值的参数

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **获取 Cell 带格式和不带格式的字符串值**
下面的示例代码解释了使用[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **控制台输出**
下面是上述示例代码的控制台输出。

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
