---
title: 添加或插入工作表
type: docs
weight: 20
url: /zh/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

在本主题中，我们将讨论使用 Aspose.Cells.GridDesktop 在 Excel 文件中添加或插入工作表的技术。添加和插入工作表的区别在于，另外，工作表只是简单地添加到Excel文件的工作表集合的末尾，而插入是将工作表添加到工作表集合中的特定位置。

{{% /alert %}} 
## **添加工作表**
要使用 Aspose.Cells.GridDesktop 添加工作表，请按照以下步骤操作：

1. 将 Aspose.Cells.GridDesktop 控件添加到窗体。
1. 在 GridDesktop 控件中调用 Worksheet 集合的 Add 方法。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Add 方法的许多重载版本都可用。例如，使用上面的重载版本，一个工作表被添加到具有默认工作表名称的 Excel 文件中。使用 Add 方法的其他重载版本，可以定义名称，如下例所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **插入工作表**
要使用 Aspose.Cells.GridDesktop 插入工作表，请按照以下步骤操作：

1. 将 Aspose.Cells.GridDesktop 控件添加到窗体。
1. 在 GridDesktop 控件中调用 Worksheets 集合的 Insert 方法。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

重要提示：Microsoft Excel (97-2003 XLS) 支持最多包含 65,536 行和 256 列的 Excel 工作表。 Aspose.Cells.GridDesktop 遵循相同的标准。在 Aspose.Cells.GridDesktop 控件中，开发人员可以添加或插入行数和列数超过标准限制的工作表，但当他们尝试将 Grid 数据保存到 Excel 文件时，将抛出异常。这意味着只有包含在 65,536 行和 256 列中的数据可以使用 Aspose.Cells.GridDesktop 保存到 Excel XLS 文件，如果您使用 XLSX（MS Excel 2007/2010）文件格式，则没有此限制。

{{% /alert %}}
