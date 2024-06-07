---
title: 从 GridWeb 导出 DataTable
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb，导出
description: 本文介绍如何在 GridWeb 中导出数据表。
---

{{% alert color="primary" %}} 

[将 DataView 导入到 GridWeb](/cells/zh/net/aspose-cells-gridweb/import-dataview-to-gridweb/) 讨论了如何将 DataView 的内容导入到 Aspose.Cells.GridWeb 控件。该主题讨论了如何将 Aspose.Cells.GridWeb 控件中的数据导出到 DataTable。

{{% /alert %}} 
## **导出工作表数据**
### **到指定的DataTable**
将工作表数据导出到特定的DataTable对象：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 创建一个特定的DataTable对象。
1. 将所选单元格的数据导出到指定的DataTable对象。

下面的示例创建一个具体的DataTable对象，有四列。工作表数据从第一个单元格开始导出，工作表中所有可见的行和列都导出到已创建的DataTable对象。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **到新的DataTable**
有时，您不想创建一个DataTable对象，而只需导出工作表数据到一个新的DataTable对象。

下面的示例尝试了一种不同的方法来展示导出方法的使用。它获取活动工作表的引用，并将该工作表的完整数据导出到一个新的DataTable对象。可以任意使用该DataTable对象。例如，可以将DataTable对象绑定到GridView以查看数据。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
