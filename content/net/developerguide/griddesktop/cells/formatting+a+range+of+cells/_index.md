---
title : "Formatting a Range of Cells" 
description : "" 
weight : 16642 
toc : false
type: docs
url: /net/developerguide/griddesktop/cells/formatting+a+range+of+cells/
---

# Aspose.Cells for .NET : Formatting a Range of Cells


This topic also belongs to the series of topics related to the application of font settings and other formatting styles on cells. Our last topics have covered well about handling such features. For example, you can refer to [Changing the Font & Color of a Cell](https://docs2.aspose.com/cells/net/developerguide/griddesktop/cells/changing+the+font+and+color+of+a+cell) and [Applying Styles on Cells](https://docs2.aspose.com/cells/net/developerguide/griddesktop/cells/applying+styles+on+cells) topics to learn about the same features. Then what is new in this topic if we have already covered these concepts. Well, the only difference of this topic with the previous ones is that we will apply formatting settings (related to fonts and other styles) on a range of cells instead of just a single cell. We hope that you will still find this topic useful for you.

## Setting Font & Style of a Range of Cells

Before we talk about formatting settings (that we have already talked a lot in our previous topics), we should know about how to create a range of cells. Well, we can create a range of cells using **CellRange** class whose constructor takes some parameters to specify the range of cells. We can specify the cells range using the **Names** or **Row & Column Indices** of start and end cells.

Once we have created a **CellRange** object then we can use the overloaded versions of **SetStyle**, **SetFont** & **SetFontColor** methods of Worksheet that can take a **CellRange** object to apply formatting settings on the specified range of cells.

Let's check out an example to understand this basic concept.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Formatting a Range of Cells-001.png](https://docs2.aspose.com/cells/net/attachments/5017782/5113880.png) (image/png)  

