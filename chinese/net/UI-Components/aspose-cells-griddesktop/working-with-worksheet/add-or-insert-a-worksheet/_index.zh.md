---
title: 添加或插入工作表
type: docs
weight: 20
url: /zh/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop，插入，工作表，插入工作表
description: 本文介绍了如何在GridDesktop中添加或插入工作表。
---

{{% alert color="primary" %}} 

在本主题中，我们将讨论使用Aspose.Cells.GridDesktop在Excel文件中添加或插入工作表的技术。添加和插入工作表的区别在于，添加工作表只是将工作表添加到Excel文件的工作表集合末尾，然而插入意味着将工作表添加到工作表集合中的特定位置。

{{% /alert %}} 
## **添加工作表**
要使用Aspose.Cells.GridDesktop添加工作表，请按照以下步骤进行：

1. 将Aspose.Cells.GridDesktop控件添加到窗体中。
1. 在GridDesktop控件中调用工作表集合的Add方法。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


有多个重载版本的Add方法可用。例如，使用上述重载版本，工作表将以默认工作表名称添加到Excel文件中。使用Add方法的其他重载版本，可以像下面的示例中那样定义名称。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **插入工作表**
要使用Aspose.Cells.GridDesktop插入工作表，请按照以下步骤进行：

1. 将Aspose.Cells.GridDesktop控件添加到窗体中。
1. 在GridDesktop控件中调用Worksheets集合的Insert方法。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

重要提示：Microsoft Excel (97-2003 XLS) 支持最多有65,536行和256列的Excel表格。Aspose.Cells.GridDesktop遵循相同的标准。在Aspose.Cells.GridDesktop控件中，开发人员可以添加或插入具有超过标准限制的行和列的工作表，但是当他们尝试将Grid数据保存到Excel文件时，将会引发异常。这意味着仅包含在65,536行和256列中的数据才能保存到Excel XLS文件中，使用XLSX (MS Excel 2007/2010)文件格式则没有此限制。

{{% /alert %}}
