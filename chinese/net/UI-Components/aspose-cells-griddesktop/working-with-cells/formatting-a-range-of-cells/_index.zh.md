---
title: 格式化一系列单元格
type: docs
weight: 60
url: /zh/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop,格式化,样式,单元格
description: 本文介绍如何在GridDesktop中对单元格应用样式格式。
---

{{% alert color="primary" %}} 

这个主题也属于与应用字体设置和其他格式样式相关的系列主题。我们之前的主题已经很好地涵盖了处理这些特性。例如，你可以参考 [更改单元格的字体和颜色](/cells/zh/net/changing-the-font-and-color-of-a-cell/) 和 [对单元格应用样式](/cells/zh/net/applying-styles-on-cells/) 主题来了解相同的特性。那么如果我们已经涵盖了这些概念，这个主题有什么新内容。嗯，这个主题与之前的不同之处在于我们将对一系列单元格应用格式设置（涉及字体和其他样式），而不仅仅是一个单个单元格。我们希望你仍然会发现这个主题对你有用。

{{% /alert %}} 
## **设置一系列单元格的字体和样式**
在我们讨论格式设置之前（我们在之前的主题中已经谈过很多），我们应该了解如何创建一系列单元格。嗯，我们可以使用**CellRange**类来创建一系列单元格，它的构造函数接受一些参数来指定单元格的范围。我们可以使用**Names**或**行列索引**来指定起始和结束单元格的范围。

一旦我们创建了**CellRange**对象，我们就可以使用Worksheet的重载版本的**SetStyle**、**SetFont**和**SetFontColor**方法，这些方法可以接受一个**CellRange**对象来应用指定范围的单元格上的格式设置。

让我们通过一个例子来了解这个基本概念。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
