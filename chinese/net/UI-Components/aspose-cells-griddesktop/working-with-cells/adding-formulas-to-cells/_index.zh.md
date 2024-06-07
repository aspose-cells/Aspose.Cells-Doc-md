---
title: 在单元格中添加公式
type: docs
weight: 30
url: /zh/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop,formula
description: 该文章介绍了如何在GridDesktop的工作表中的单元格中设置或获取公式。
---

{{% alert color="primary" %}} 

一个单元格不仅可以包含简单值，如数值或一些文本，还可以包含公式作为其值。当单元格的值需要在一些计算之后确定时，就会在单元格中使用公式。在本主题中，我们将讨论如何访问和修改应用于单元格的公式。

{{% /alert %}} 
## **向单元格添加公式**
向单元格添加公式就像我们在之前的主题中讨论的设置单元格值一样：[访问和修改单元格的值](/cells/zh/net/accessing-and-modifying-the-value-of-a-cell/),只是在那种情况下，我们只向单元格添加了简单值。现在，我们将添加公式。开发人员可以使用单元格的Value属性来访问和修改公式，否则也可以使用单元格的**SetCellValue**方法来向单元格添加或修改公式。

**重要:** 使用Value属性或单元格的**SetCellValue**方法之间的基本区别在于Value属性会自动调用Grid的**RunAllFormulas**方法来重新计算所有公式的值，而在**SetCellValue**方法的情况下，开发人员需要在向单元格添加公式后显式调用**RunAllFormulas**方法。实际上，当使用单元格的**SetCellValue**方法时，此方法仅将单元格的值设置为**FormulaType**，而不计算公式。此外，每次调用**RunAllFormulas**方法都是不必要的。如果要在工作表的单元格中添加多个公式，则可以在最后只调用一次**RunAllFormulas**方法。

公式作为字符串值添加到单元格中。此外，公式结构必须与MS Excel的公式结构兼容。所有公式必须以**等号（=）**开头。

在下面的示例中，我们添加了一个公式，用于将工作表中的两个单元格的值相乘，并将结果存储到另一个单元格中。最后还调用了**RunAllFormulas**方法。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



现在运行应用程序。如果双击添加了公式的单元格，则会注意到值将被公式替换，该公式实际上正在后台计算值。

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop支持MS Excel的大多数常用函数。有关受支持函数列表的更多详情，请[点击这里](/cells/zh/net/list-of-supported-functions/)。

{{% /alert %}}
