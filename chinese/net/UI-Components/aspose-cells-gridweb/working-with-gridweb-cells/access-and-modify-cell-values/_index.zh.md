---
title: 访问和修改单元格值
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb,单元格值,修改,值
description: 本文介绍了如何在GridWeb中获取和修改单元格值。
---

{{% alert color="primary" %}} 

[访问工作表单元格](/cells/zh/net/aspose-cells-gridweb/access-worksheet-cells/)讨论了如何访问单元格。本主题扩展了该讨论，展示了如何使用Aspose.Cells.GridWeb API访问和修改单元格值。

{{% /alert %}} 
## **访问和修改单元格的值**
### **字符串值**
在访问和修改单元格值之前，您需要了解如何访问单元格。有关访问单元格的不同方法的详细信息，请参阅[访问工作表单元格](/cells/zh/net/aspose-cells-gridweb/access-worksheet-cells/)。

每个单元格都有一个名为StringValue的属性。一旦访问到单元格，开发人员可以使用StringValue属性访问单元格的字符串值。要修改单元格值，提供了一个名为PutValue的特殊方法，可用于更新单元格的字符串值。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **所有类型的值**
单元格对象的PutValue方法有8个可用的重载，可用于修改单元格中的任何类型的值（布尔值、整数、双精度浮点数、日期时间和字符串）。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



PutValue方法还有一个重载版本，可以接受以字符串格式表示的任何类型的值，并自动将其转换为适当的数据类型。要实现此目的，请将布尔值true传递给PutValue方法的另一个参数，如下例所示。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
