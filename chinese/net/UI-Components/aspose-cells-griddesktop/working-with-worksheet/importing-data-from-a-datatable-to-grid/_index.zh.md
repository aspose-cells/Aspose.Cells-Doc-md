---
title: 从DataTable导入数据到Grid
type: docs
weight: 50
url: /zh/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop,导入,数据,DataTable
description: 这篇文章介绍了如何在GridDesktop中导入数据。
---

{{% alert color="primary" %}} 

自.NET Framework发布以来，微软提供了一种极好的离线存储数据的方式，即DataTable对象。了解开发人员的需求，Aspose.Cells.GridDesktop也支持从数据表导入数据。本主题讨论了如何实现此操作。

{{% /alert %}} 
## **例子**
使用Aspose.Cells.GridDesktop控件导入数据表内容的步骤：

1. 将Aspose.Cells.GridDesktop控件添加到窗体中。
1. 创建一个包含要导入的数据的DataTable对象。
1. 获取所需工作表的引用。
1. 将数据表内容导入到工作表中。
1. 根据数据表的列名设置工作表的列标题。
1. 如果需要，设置列的宽度。
1. 显示工作表。

在下面的示例中，我们创建了一个DataTable对象，并填充了一些从名为Products的数据库表中获取的数据。最后，我们使用Aspose.Cells.GridDesktop将数据从该DataTable对象导入到所需的工作表中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
