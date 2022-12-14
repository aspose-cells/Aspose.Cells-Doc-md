---
title: 将数据从 DataTable 导入到网格
type: docs
weight: 50
url: /zh/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

自 .NET Framework 发布以来，Microsoft 提供了一种以 DataTable 对象的形式在离线模式下存储数据的绝佳方式。了解开发者的需求，Aspose.Cells.GridDesktop也支持从数据表中导入数据。本主题讨论如何执行此操作。

{{% /alert %}} 
## **例子**
使用 Aspose.Cells.GridDesktop 控件导入数据表的内容：

1. 将 Aspose.Cells.GridDesktop 控件添加到窗体。
1. 创建一个包含要导入的数据的 DataTable 对象。
1. 获取所需工作表的引用。
1. 将数据表内容导入工作表。
1. 根据数据表的列名设置工作表的列标题。
1. 如果需要，设置列的宽度/
1. 显示工作表。

在下面给出的示例中，我们创建了一个 DataTable 对象并用从名为 Products 的数据库表中获取的一些数据填充它。最后，我们使用 Aspose.Cells.GridDesktop 将数据从该 DataTable 对象导入到所需的工作表中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
