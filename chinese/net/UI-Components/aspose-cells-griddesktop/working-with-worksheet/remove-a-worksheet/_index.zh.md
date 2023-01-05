---
title: 删除工作表
type: docs
weight: 30
url: /zh/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

本主题讨论使用 Aspose.Cells.GridDesktop 控件删除工作表。有几种简单的方法可以完成这项基本任务。

{{% /alert %}} 
## **删除工作表**
要使用 Aspose.Cells.GridDesktop 控件删除工作表，请按照以下步骤操作：

1. 将 Aspose.Cells.GridDesktop 控件添加到窗体。
1. 在 GridDesktop 控件中调用 Worksheets 集合的 Remove 方法。
### **使用工作表索引**
在这种方法中，只需传递要删除的工作表的工作表索引（在网格的工作表集合中）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **使用工作表名称**
如果已知工作表的名称，则可以通过指定其名称来删除特定的工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

删除是一种方法。使用它可以使用其索引（在工作表集合中）删除工作表，或使用 RemoveAt 方法使用其索引/名称删除工作表。

{{% /alert %}}
