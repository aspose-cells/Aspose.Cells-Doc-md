---
title: 通过Aspose.Cells自动刷新OLE对象通过Microsoft Excel
type: docs
weight: 270
url: /zh/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells提供了[**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload)属性，在Microsoft Excel中打开Excel文件时刷新OLE对象。由于这个属性，OLE对象将显示Microsoft Excel生成的正确OLE图像。

{{% /alert %}}

以下示例代码加载了有一个非真实OLE图像的 [示例 Excel 文件](5115231.xlsx)。OLE对象实际上是一个 Microsoft Word 文档，但示例 Excel 文件显示的是动物图像而不是 Microsoft Word 图像。但是，如果您打开[输出的 Excel 文件](5115225.xlsx)，您将看到 Microsoft Excel 显示正确的 OLE 图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
