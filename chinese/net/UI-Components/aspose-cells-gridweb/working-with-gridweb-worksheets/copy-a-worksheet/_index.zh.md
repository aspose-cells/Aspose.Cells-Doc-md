---
title: 复制工作表
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb, 复制, GridWorksheet
description: 本文介绍了如何在GridWeb中复制工作表（GridWorksheet）。
---

{{% alert color="primary" %}} 

[添加工作表](/cells/zh/net/aspose-cells-gridweb/add-worksheets/)描述了如何向Aspose.Cells.GridWeb添加新工作表。还可以将另一工作表的复制（或副本）添加到Aspose.Cells.GridWeb控件。当需要在另一个工作表中也需要相同或类似的数据时，复制现有工作表并将其添加到Aspose.Cells.GridWeb作为新工作表会更加方便，而不是从头开始创建。

{{% /alert %}} 
## **复制工作表**
### **使用Sheet索引**
下面的示例代码显示了如何通过指定工作表在GridWorksheetCollection的AddCopy方法中的索引，将工作表的副本添加到GridWeb控件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **使用工作表名称**
下面的示例代码显示了如何通过指定工作表在GridWorksheetCollection的AddCopy方法中的名称，将工作表的副本添加到GridWeb控件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

AddCopy方法返回新添加的工作表的索引，可以用于访问工作表实例。有关如何访问工作表的详细信息，请阅读[访问工作表](/cells/zh/net/aspose-cells-gridweb/access-worksheets/)。

{{% /alert %}}
