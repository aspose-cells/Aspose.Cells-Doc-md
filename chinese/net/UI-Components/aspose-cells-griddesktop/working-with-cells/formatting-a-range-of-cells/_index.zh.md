---
title: 格式化 Cells 的范围
type: docs
weight: 60
url: /zh/net/formatting-a-range-of-cells/
---
{{% alert color="primary" %}} 

本主题还属于与在单元格上应用字体设置和其他格式样式相关的系列主题。我们的最后一个主题已经很好地涵盖了如何处理此类功能。例如，您可以参考[更改 Cell 的字体和颜色](/cells/zh/net/changing-the-font-and-color-of-a-cell/)和[在 Cells 上应用样式](/cells/zh/net/applying-styles-on-cells/)主题以了解相同的功能。如果我们已经涵盖了这些概念，那么本主题的新内容是什么。好吧，本主题与之前主题的唯一区别是我们将在一系列单元格而不是单个单元格上应用格式设置（与字体和其他样式相关）。我们希望您仍然会发现该主题对您有用。

{{% /alert %}} 
## **设置 Cells 范围的字体和样式**
在我们讨论格式设置（我们在之前的主题中已经讨论过很多）之前，我们应该了解如何创建一系列单元格。好吧，我们可以使用创建一系列单元格**单元格范围**其构造函数采用一些参数来指定单元格范围的类。我们可以使用**名称**要么**行和列索引**开始和结束细胞。

一旦我们创建了一个**单元格范围**对象，那么我们可以使用的重载版本**设置样式**, **设置字体** & **设置字体颜色**工作表的方法，可以采取**单元格范围**对象以在指定范围的单元格上应用格式设置。

让我们看一个例子来理解这个基本概念。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
