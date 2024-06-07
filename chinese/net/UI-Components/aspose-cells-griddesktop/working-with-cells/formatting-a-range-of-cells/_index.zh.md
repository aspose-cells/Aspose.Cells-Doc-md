---
title: 格式化一系列单元格
type: docs
weight: 60
url: /zh/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop,格式,风格,单元格
description: 本文介绍了如何在GridDesktop中的单元格上应用样式格式。
---

{{% alert color="primary" %}} 

此主题也属于与在单元格上应用字体设置和其他格式样式相关的系列主题。 我们上一个主题已经很好地涵盖了处理这些功能。 例如，您可以参考[更改单元格的字体和颜色](/cells/zh/net/changing-the-font-and-color-of-a-cell/)和[在单元格上应用样式](/cells/zh/net/applying-styles-on-cells/)主题了解有关相同功能的信息。 然而，如果我们已经涵盖了这些概念，那么这个主题的新鲜之处在哪里。 好吧，与以前的主题相比，这个主题的唯一区别是我们将在一系列单元格而不仅仅是单个单元格上应用格式设置(涉及字体和其他样式)。 我们希望您仍然会发现这个主题对您有用。

{{% /alert %}} 
## **设置单元格范围的字体和样式**
在我们讨论格式设置之前（我们在以前的主题中已经谈论了很多），我们应该知道如何创建单元格范围。嗯，我们可以使用**CellRange**类创建单元格范围，其构造函数采用一些参数来指定单元格范围。我们可以使用**名称**或**起始和结束单元格的行列索引**指定单元格范围。

创建了**CellRange**对象后，我们可以使用Worksheet的重载版本的**SetStyle**，**SetFont**和**SetFontColor**方法，这些方法可以接受**CellRange**对象，以应用指定单元格范围的格式设置。

让我们看一个例子来理解这个基本概念。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
