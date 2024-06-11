---
title: 将 DataView 导入到 GridWeb
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb，导入
description: 本文介绍了如何在 GridWeb 中导入数据。
---

{{% alert color="primary" %}} 

随着 Microsoft .NET Framework 的发布，引入了一种新的存储数据的方式。现在能够使用 DataSet、DataTable 和 DataView 对象以离线模式存储数据。这些对象非常方便，可作为数据存储库。使用 Aspose.Cells.GridWeb，可以从 DataTable 或 DataView 对象中导入数据到工作表。Aspose.Cells.GridWeb 仅支持从 DataView 中导入数据，但 DataTable 对象也可以间接使用。让我们详细讨论此功能。

{{% /alert %}} 
## **从 DataView 导入数据**
使用 GridWeb 控件中的 GridWorsheetCollection 的 ImportDataView 方法从 DataView 对象中导入数据。将要导入数据的 DataView 对象传递给 ImportDataView 方法。在导入期间可以指定列标题和数据样式。

{{% alert color="primary" %}} 

从 DataView 对象导入数据时，将创建一个新的工作表来保存导入的数据。该工作表与 DataTable 同名。

{{% /alert %}} 

**输出：从 DataView 导入的数据到新工作表** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

调整列宽以显示它们包含的所有数据。在从 DataView 导入数据时，列宽不会自动调整。用户需要自行调整它们。要通过编程方式调整列宽，请参阅[调整行和列大小](/cells/zh/net/aspose-cells-gridweb/resize-rows-and-columns/)。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

ImportDataView 方法的重载版本允许开发人员指定保存导入数据的工作表的名称，以及从 DataView 对象中导入的特定行数和列数。

{{% /alert %}}
