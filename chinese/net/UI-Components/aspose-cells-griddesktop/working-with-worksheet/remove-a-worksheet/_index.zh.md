---
title: 移除工作表
type: docs
weight: 30
url: /zh/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop,移除,工作表
description: 本文介绍了如何在GridDesktop中移除工作表。
---

{{% alert color="primary" %}} 

本主题讨论了使用Aspose.Cells.GridDesktop控件移除工作表的几种简单方法。

{{% /alert %}} 
## **移除工作表**
要使用Aspose.Cells.GridDesktop控件移除工作表，请执行以下步骤：

1. 将Aspose.Cells.GridDesktop控件添加到窗体中。
1. 在GridDesktop控件中调用Worksheets集合的Remove方法。
### **使用工作表索引**
在此方法中，只需传递要删除的工作表的工作表索引（在网格的工作表集合中）。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **使用工作表名称**
如果知道工作表的名称，则可以通过指定其名称来删除特定的工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Remove是一个方法。 使用它可以使用其索引（在工作表集合中）删除工作表，或者使用RemoveAt方法使用其索引/名称删除工作表。

{{% /alert %}}
