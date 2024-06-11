---
title: 添加单元格公式
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb,公式
description: 本文介绍了如何在GridWeb中的单元格中添加公式。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 提供的最有价值的功能是支持公式或函数。Aspose.Cells.GridWeb 有自己的公式引擎，用于计算工作表中的公式。Aspose.Cells.GridWeb 支持内置和用户定义的函数或公式。本主题详细讨论了使用 Aspose.Cells.GridWeb API 向单元格添加公式。

{{% /alert %}} 
## **向单元格添加公式**
### **如何添加和计算公式？**
可以通过使用单元格的Formula属性来添加、访问和修改单元格中的公式。Aspose.Cells.GridWeb支持从简单到复杂的用户定义公式。然而，Aspose.Cells.GridWeb还提供了大量的类似于Microsoft Excel的内置函数或公式。要查看完整的内置函数列表，请参考[支持的函数列表。](/cells/zh/net/aspose-cells-gridweb/list-of-supported-functions/)

{{% alert color="primary" %}} 

公式语法应与 Microsoft Excel 语法兼容。例如，所有公式必须以等号（=）开头。

要动态添加公式，Aspose.Cells.GridWeb将把它识别为公式，即使您没有使用**=**号，但如果终端用户在GUI中工作，他必须使用"="号。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**将公式添加到 B3 单元格，但未由 GridWeb 计算** 

![todo:image_alt_text](add-cell-formulas_1.png)

在上面的屏幕截图中，您可以看到已经在B3单元格中添加了一个公式，但尚未计算。要计算所有公式，请在向工作表添加公式后，调用GridWeb控件的GridWorksheetCollection的CalculateFormula方法。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

用户还可以通过单击 **提交** 来计算公式。

**单击 GridWeb 的提交按钮** 

![todo:image_alt_text](add-cell-formulas_2.png)

**重要**：如果用户单击 **保存** 或 **撤销** 按钮，或者工作表标签，则所有公式将由 GridWeb 自动计算。

**计算后的公式结果** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **引用其他工作表中的单元格**
使用 Aspose.Cells.GridWeb，可以在其公式中引用存储在不同工作表中的值，从而创建复杂的公式。

从不同工作表引用单元格值的语法是 SheetName!CellName。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
