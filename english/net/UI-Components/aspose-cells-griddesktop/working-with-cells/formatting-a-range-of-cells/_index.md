---
title: Formatting a Range of Cells
type: docs
weight: 60
url: /net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop,format,style,cells
description: This article introduces how to apply style format on cells in GridDesktop.
---

{{% alert color="primary" %}} 

This topic also belongs to the series of topics related to the application of font settings and other formatting styles on cells. Our last topics have covered well about handling such features. For example, you can refer to [Changing the Font & Color of a Cell](/cells/net/changing-the-font-and-color-of-a-cell/) and [Applying Styles on Cells](/cells/net/applying-styles-on-cells/) topics to learn about the same features. Then what is new in this topic if we have already covered these concepts. Well, the only difference of this topic with the previous ones is that we will apply formatting settings (related to fonts and other styles) on a range of cells instead of just a single cell. We hope that you will still find this topic useful for you.

{{% /alert %}} 
## **Setting Font & Style of a Range of Cells**
Before we talk about formatting settings (that we have already talked a lot in our previous topics), we should know about how to create a range of cells. Well, we can create a range of cells using **CellRange** class whose constructor takes some parameters to specify the range of cells. We can specify the cells range using the **Names** or **Row & Column Indices** of start and end cells.

Once we have created a **CellRange** object then we can use the overloaded versions of **SetStyle**, **SetFont** & **SetFontColor** methods of Worksheet that can take a **CellRange** object to apply formatting settings on the specified range of cells.

Let's check out an example to understand this basic concept.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
