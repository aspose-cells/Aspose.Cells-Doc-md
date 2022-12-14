---
title: 将公式添加到 Cells
type: docs
weight: 30
url: /zh/net/adding-formulas-to-cells/
---
{{% alert color="primary" %}} 

一个单元格不仅可以包含一个简单的值，比如数字或一些文本，我们还可以在单元格中插入一个公式作为它的值。当需要在一些计算之后确定单元格的值时，在单元格中使用公式。在本主题中，我们将讨论如何访问和修改应用于单元格的公式。

{{% /alert %}} 
## **将公式添加到 Cell**
向单元格添加公式就像我们在上一个主题中讨论的设置单元格的值一样：[访问和修改 Cell 的值](/cells/zh/net/accessing-and-modifying-the-value-of-a-cell/)除了在那种情况下，我们只是向单元格添加了简单的值。现在，我们将添加公式。开发人员可以使用单元格的 Value 属性来访问和修改公式或以其他方式**设置单元格值**单元格的方法也可用于在单元格中添加或修改公式。

**重要的：**使用 Value 属性或**设置单元格值**单元格的方法是 Value 属性调用**运行所有公式**Grid 的方法自动重新计算所有公式的值，如**设置单元格值**开发者需要调用的方法**运行所有公式**将公式添加到单元格后显式方法。实际上，当我们使用**设置单元格值**单元格的方法然后此方法将单元格的值设置为**公式类型**仅且不计算公式。此外，调用**运行所有公式**方法每次都没有必要。如果你想在工作表的单元格中添加许多公式，那么你可以调用**运行所有公式**方法最后一次。

公式作为字符串值添加到单元格。此外，公式结构必须与 MS Excel 的公式结构兼容。所有公式必须以**等号 (=)**.

在下面给出的示例中，我们添加了一个公式来将工作表中两个单元格的值相乘，并将结果存储到另一个单元格中。**运行所有公式**方法也在最后被调用。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



现在运行应用程序。如果双击添加公式的单元格，您会注意到该值将被实际计算后端值的公式替换。

{{% alert color="primary" %}} 

 Aspose.Cells.GridDesktop支持MS Excel的大部分常用功能。有关支持功能列表的更多详细信息，请[点击这里。](/cells/zh/net/list-of-supported-functions/)

{{% /alert %}}
