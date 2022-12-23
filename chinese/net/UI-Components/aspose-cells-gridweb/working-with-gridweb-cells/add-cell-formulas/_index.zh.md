---
title: 添加 Cell 公式
type: docs
weight: 30
url: /zh/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 提供的最有价值的功能是支持公式或函数。 Aspose.Cells.GridWeb 有自己的公式引擎，可以计算工作表中的公式。 Aspose.Cells.GridWeb 支持内置和用户定义的函数或公式。本主题详细讨论使用 Aspose.Cells.GridWeb API 向单元格添加公式。

{{% /alert %}} 
## **将公式添加到 Cells**
### **如何添加和计算公式？**
可以使用单元格的公式属性在单元格中添加、访问和修改公式。 Aspose.Cells.GridWeb支持从简单到复杂的用户自定义公式。但是，Aspose.Cells.GridWeb也提供了大量的内置函数或公式（类似于Microsoft Excel）。要查看内置函数的完整列表，请参阅此[支持的功能列表。](/cells/zh/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

公式语法应与 Microsoft Excel 语法兼容。例如，所有公式都必须以等号 (=) 开头。

要动态添加公式，Aspose.Cells.GridWeb 即使您不使用 **=** 符号也会将其识别为公式，但如果最终用户在 GUI 中工作，他必须使用“=”符号。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**公式添加到 B3 单元格但未由 GridWeb 计算** 

![待办事项：图片_替代_文本](add-cell-formulas_1.png)

在上面的截图中，可以看到B3中已经添加了一个公式，但是还没有进行计算。要计算所有公式，请在将公式添加到工作表后调用 GridWeb 控件的 GridWorksheetCollection 的 CalculateFormula 方法，如下所示。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

用户还可以通过单击计算公式**提交**.

**单击 GridWeb 的提交按钮** 

![待办事项：图片_替代_文本](add-cell-formulas_2.png)

**重要的**：如果用户点击**救球**要么**撤消**按钮或工作表选项卡，所有公式均由 GridWeb 自动计算。

**计算后的公式结果** 

![待办事项：图片_替代_文本](add-cell-formulas_3.png)

{{% /alert %}} 
### **从其他工作表中引用 Cells**
使用 Aspose.Cells.GridWeb，可以在其公式中引用存储在不同工作表中的值，从而创建复杂的公式。

从不同工作表引用单元格值的语法是 SheetName!CellName。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
