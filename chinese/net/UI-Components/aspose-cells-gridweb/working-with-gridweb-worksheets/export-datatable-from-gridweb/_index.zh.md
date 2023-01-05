---
title: 从 GridWeb 导出数据表
type: docs
weight: 70
url: /zh/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[将 DataView 导入 GridWeb](/cells/zh/net/import-dataview-to-gridweb/)谈到将 DataView 的内容导入 Aspose.Cells.GridWeb 控件。本主题讨论将数据从 Aspose.Cells.GridWeb 控件导出到 DataTable。

{{% /alert %}} 
## **导出工作表数据**
### **到特定的数据表**
将工作表数据导出到特定的 DataTable 对象：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 创建特定的 DataTable 对象。
1. 将选中单元格的数据导出到指定的DataTable对象中。

下面的示例创建了一个具有四列的特定 DataTable 对象。工作表数据从工作表中所有行和列都可见的第一个单元格开始导出到已创建的 DataTable 对象。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **到一个新的数据表**
有时，您不想创建 DataTable 对象，而只是需要将工作表数据导出到新的 DataTable 对象。

下面的例子尝试了一种不同的方式来展示 Export 方法的使用。它引用活动工作表并将该工作表的完整数据导出到新的 DataTable 对象。 DataTable 对象现在可以按您想要的任何方式使用。例如，可以将 DataTable 对象绑定到 GridView 以查看数据。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
