---
title: 删除工作表
type: docs
weight: 30
url: /zh/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop,删除,工作表
description: 本文介绍了如何在GridDesktop中删除工作表。
---

{{% alert color="primary" %}} 

本主题讨论了使用Aspose.Cells.GridDesktop控件删除工作表。有几种简单的方法来完成这个基本任务。

{{% /alert %}} 
## **删除工作表**
要使用Aspose.Cells.GridDesktop控件删除工作表，请按照以下步骤：

1. 在表单中添加 Aspose.Cells.GridDesktop 控件。
1. 在 GridDesktop 控件中调用 Worksheets 集合的 Remove 方法。
### **使用工作表索引**
使用这种方法，只需将要删除的工作表的索引（在网格的工作表集合中）传递给它。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **使用工作表名称**
如果知道工作表的名称，则可以通过指定其名称来删除特定的工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Remove 是一个方法。 使用它来删除工作表（使用工作表集合中的索引），或使用 RemoveAt 方法来删除工作表（使用索引/名称）。

{{% /alert %}}
