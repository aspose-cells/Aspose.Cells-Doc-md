---
title: 将 DataView 导入 GridWeb
type: docs
weight: 60
url: /zh/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

随着 Microsoft .NET Framework 的发布，引入了一种新的数据存储方式。现在 DataSet、DataTable 和 DataView 对象以离线模式存储数据。这些对象作为数据存储库非常方便。使用 Aspose.Cells.GridWeb，可以将数据从 DataTable 或 DataView 对象导入到工作表中。 Aspose.Cells.GridWeb只支持从DataView导入数据。对象，但也可以间接使用 DataTable 对象。让我们详细讨论这个特性。

{{% /alert %}} 
## **从 DataView 导入数据**
使用 GridWeb 控件中的 GridWorsheetCollection 的 ImportDataView 方法从 DataView 对象导入数据。将要从中导入数据的 DataView 对象传递给 ImportDataView 方法。可以在导入期间指定列标题和数据样式。

{{% alert color="primary" %}} 

从 DataView 对象导入数据时，会创建一个新工作表来保存导入的数据。工作表的名称与 DataTable 的名称相同。

{{% /alert %}} 

**输出：从 DataView 导入到新工作表中的数据** 

![待办事项：图片_替代_文本](import-dataview-to-gridweb_1.png)

调整列的宽度以显示它们包含的所有数据。从 DataView 导入数据时，不会自动调整列宽。用户需要自行调整。要以编程方式调整列宽，请参阅[调整行和列的大小](/cells/zh/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

ImportDataView 方法的重载版本允许开发人员指定保存导入数据的工作表的名称以及要从 DataView 对象导入的特定行数和列数。

{{% /alert %}}
