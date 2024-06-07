---
title: 将DataView导入GridWeb
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb，导入
description: 本文介绍了如何在GridWeb中导入数据。
---

{{% alert color="primary" %}} 

随着微软.NET Framework的发布，引入了一种新的存储数据的方式。现在可以使用离线模式存储数据的DataSet、DataTable和DataView对象。这些对象非常方便作为数据存储库。使用Aspose.Cells.GridWeb，可以从DataTable或DataView对象中导入数据到工作表。Aspose.Cells.GridWeb仅支持从DataView中导入数据对象，但DataTable对象也可以间接使用。我们将详细讨论此功能。

{{% /alert %}} 
## **从DataView导入数据**
使用GridWeb控件中GridWorsheetCollection的ImportDataView方法从DataView对象导入数据。将要从中导入数据的DataView对象传递给ImportDataView方法。在导入时可以指定列标题和数据样式。

{{% alert color="primary" %}} 

当从DataView对象导入数据时，将创建一个新的工作表来保存导入的数据。工作表的名称与DataTable相同。

{{% /alert %}} 

**输出: 从DataView导入数据到新的工作表** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

调整列的宽度以显示其包含的所有数据。当从DataView导入数据时，列宽不会自动调整。用户需要自行调整它们。要以编程方式调整列宽，请参考[调整行和列大小](/cells/zh/net/aspose-cells-gridweb/resize-rows-and-columns/)。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

ImportDataView方法的重载版本允许开发人员指定保存导入数据的工作表的名称以及从DataView对象导入的特定行数和列数。

{{% /alert %}}
