---
title: 从DataTable导入数据到Grid
type: docs
weight: 50
url: /zh/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop，导入，数据，DataTable
description: 本文介绍了如何在GridDesktop中导入数据。
---

{{% alert color="primary" %}} 

自.NET框架发布以来，微软已经提供了一种优秀的方式，以DataTable对象的形式在离线模式下存储数据。为了满足开发者的需求，Aspose.Cells.GridDesktop也支持从数据表中导入数据。本主题讨论了如何做到这一点。

{{% /alert %}} 
## **示例**
使用Aspose.Cells.GridDesktop控件导入数据表内容:

1. 将Aspose.Cells.GridDesktop控件添加到表单中。
1. 创建包含要导入的数据的DataTable对象。
1. 获取所需工作表的引用。
1. 将数据表内容导入工作表。
1. 根据数据表的列名设置工作表的列标题。
1. 如有需要，设置列的宽度。
1. 显示工作表。

在下面的示例中，我们创建了一个DataTable对象，并填充了一些来自名为Products的数据库表的数据。最后，我们使用Aspose.Cells.GridDesktop从该DataTable对象导入数据到所需的工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
