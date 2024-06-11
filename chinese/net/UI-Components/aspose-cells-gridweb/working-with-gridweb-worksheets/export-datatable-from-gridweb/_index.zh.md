---
title: 从 GridWeb 导出 DataTable
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb，导出
description: 本文介绍了如何在 GridWeb 中导出 DataTable。
---

{{% alert color="primary" %}} 

[将 DataView 导入到 GridWeb](/cells/zh/net/aspose-cells-gridweb/import-dataview-to-gridweb/)讨论了将 DataView 的内容导入到 Aspose.Cells.GridWeb 控件。本主题讨论了将来自 Aspose.Cells.GridWeb 控件的数据导出到 DataTable。

{{% /alert %}} 
## **导出工作表数据**
### **导出到特定的 DataTable**
将工作表数据导出到特定的 DataTable 对象：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 创建特定的 DataTable 对象。
1. 将选定单元格的数据导出到指定的 DataTable 对象。

下面的示例创建一个具有四列的特定 DataTable 对象。工作表数据从第一个单元格开始导出，工作表中所有可见的行和列都导出到已创建的 DataTable 对象。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **导出到新的 DataTable**
有时，您不想创建 DataTable 对象，而只需将工作表数据导出到新的 DataTable 对象。

下面的示例尝试以不同方式展示 Export 方法的使用。它获取活动工作表的引用，将该工作表的完整数据导出到新的 DataTable 对象。现在可以以任何方式使用 DataTable 对象。例如，可以将 DataTable 对象绑定到 GridView 以查看数据。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
