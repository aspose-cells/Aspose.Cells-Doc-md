---
title: 在单元格中添加公式
type: docs
weight: 30
url: /zh/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop, 公式
description: 本文介绍如何在GridDesktop的工作表中的单元格中获取或设置公式。
---

{{% alert color="primary" %}} 

单元格不仅可以包含简单的值，如数值或文本，还可以包含公式作为其值。当单元格的值需要在进行一些计算后确定时，就会在单元格中使用公式。在本主题中，我们将讨论如何访问和修改应用于单元格的公式。

{{% /alert %}} 
## **向单元格添加公式**
向单元格添加公式就像我们在之前的主题中讨论的将单元格值设置为一样： 访问和修改单元格的值，只是在那种情况下，我们只是向单元格添加了简单的值。现在，我们将添加公式。开发人员可以使用单元格的Value属性来访问和修改公式，否则也可以使用单元格的 SetCellValue 方法向单元格添加或修改公式。

重要提示：使用单元格的Value属性或SetCellValue方法之间的基本差异在于，Value属性会自动调用Grid的RunAllFormulas方法来重新计算所有公式的值，而对于SetCellValue方法，开发人员需要在向单元格添加公式后显式调用RunAllFormulas方法。实际上，当使用SetCellValue方法向单元格添加公式时，此方法将单元格的值设置为FormulaType，并不计算公式。此外，每次都调用RunAllFormulas方法并非必要。如果要在工作表的单元格中添加多个公式，则可以在最后仅调用一次RunAllFormulas方法。

公式被添加到单元格作为字符串值。此外，公式结构必须与MS Excel的公式结构兼容。所有的公式都必须以等号（=）开头。

在下面的示例中，我们添加了一个公式，用于将工作表的两个单元格的值相乘，并将结果存储到另一个单元格中。最后还调用了RunAllFormulas方法。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



现在运行应用程序。如果您双击添加了公式的单元格，则会注意到值将被计算值替换，该计算值实际上是在后端进行计算的公式。

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop支持MS Excel的大多数常用函数。有关支持功能列表的更多详细信息，请[点击这里](/cells/zh/net/list-of-supported-functions/)

{{% /alert %}}
