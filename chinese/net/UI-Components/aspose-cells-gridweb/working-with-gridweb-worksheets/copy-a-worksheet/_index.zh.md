---
title: 复制工作表
type: docs
weight: 50
url: /zh/net/copy-a-worksheet/
---
{{% alert color="primary" %}} 

[添加工作表](/cells/zh/net/add-worksheets/)介绍如何向 Aspose.Cells.GridWeb 添加新工作表。也可以将另一个工作表的副本（或副本）添加到 Aspose.Cells.GridWeb 控件。当一个工作表中的相同或相似数据在另一个工作表中也需要时，此功能会很有用。在这种情况下，复制现有工作表并将其作为新工作表添加到 Aspose.Cells.GridWeb 比从头开始创建更容易。

{{% /alert %}} 
## **复制工作表**
### **使用工作表索引**
下面的示例代码显示了如何通过在 GridWorksheetCollection 的 AddCopy 方法中指定工作表的索引来将工作表的副本添加到 GridWeb 控件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **使用工作表名称**
下面的示例代码显示了如何通过在 GridWorksheetCollection 的 AddCopy 方法中指定工作表的名称来将工作表的副本添加到 GridWeb 控件。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

 AddCopy 方法返回新添加的工作表的索引，可用于访问工作表实例。有关如何访问工作表的更多详细信息，请阅读[访问工作表](/cells/zh/net/access-worksheets/).

{{% /alert %}}
