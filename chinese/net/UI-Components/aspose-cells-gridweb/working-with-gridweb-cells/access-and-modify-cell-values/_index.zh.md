---
title: 访问和修改 Cell 值
type: docs
weight: 20
url: /zh/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[访问工作表 Cells](/cells/zh/net/access-worksheet-cells/)讨论了访问单元格。本主题扩展该讨论以显示如何使用 Aspose.Cells.GridWeb API 访问和修改单元格值。

{{% /alert %}} 
## **访问和修改 Cell 的值**
### **字符串值**
在访问和修改单元格的值之前，您需要知道如何访问单元格。有关访问单元格的不同方法的详细信息，请参阅[访问工作表 Cells](/cells/zh/net/access-worksheet-cells/).

每个单元格都有一个名为 StringValue 的属性。访问单元格后，开发人员可以使用 StringValue 属性访问单元格字符串值。为了修改单元格值，提供了一种特殊方法 PutValue，可用于更新单元格的字符串值。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **所有类型的值**
单元格对象的 PutValue 方法有 8 个可用重载，可用于修改单元格中的任何类型的值（布尔值、整数、双精度值、日期时间和字符串）。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



还有一个 PutValue 方法的重载版本，它可以采用字符串格式的任何类型的值并自动将其转换为适当的数据类型。为此，将布尔值 true 传递给 PutValue 方法的另一个参数，如下例所示。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
