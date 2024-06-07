---
title: 复制工作表
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/copy-a-worksheet/
keywords: GridWeb，复制，GridWorksheet
description: 本文介绍了如何在GridWeb中复制工作表（GridWorksheet）。
---

{{% alert color="primary" %}} 

[添加工作表](/cells/zh/net/aspose-cells-gridweb/add-worksheets/)描述了如何向Aspose.Cells.GridWeb添加新的工作表。还可以添加另一个工作表的副本或复制到Aspose.Cells.GridWeb控件中。当一个工作表中需要另一个工作表中的相同或相似数据时，复制现有工作表并将其作为新工作表添加到Aspose.Cells.GridWeb比从头开始创建更容易。

{{% /alert %}} 
## **复制工作表**
### **使用表索引**
下面的示例代码展示了如何通过在GridWorksheetCollection的AddCopy方法中指定工作表的索引来将工作表的副本添加到GridWeb控件中。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **使用工作表名称**
下面的示例代码展示了如何通过在GridWorksheetCollection的AddCopy方法中指定工作表名称将工作表的副本添加到GridWeb控件中。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

AddCopy方法返回新添加的工作表的索引，可以用来访问工作表实例。要了解更多关于如何访问工作表的详细信息，请阅读[访问工作表](/cells/zh/net/aspose-cells-gridweb/access-worksheets/)。

{{% /alert %}}
