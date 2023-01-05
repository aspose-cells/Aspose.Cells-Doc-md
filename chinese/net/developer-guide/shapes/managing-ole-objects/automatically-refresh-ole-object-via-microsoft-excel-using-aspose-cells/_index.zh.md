---
title: 使用 Aspose.Cells 通过 Microsoft Excel 自动刷新 OLE 对象
type: docs
weight: 270
url: /zh/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---
{{% alert color="primary" %}}

Aspose.Cells 提供了[**OleObject.自动加载**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload)在 Microsoft Excel 中打开 excel 文件时刷新 OLE 对象的属性。由于此属性，OLE 对象将显示由 Microsoft Excel 生成的正确 OLE 图像。

{{% /alert %}}

下面的示例代码加载[示例 excel 文件](5115231.xlsx)它有一个非真实的 OLE 图像。 OLE 对象实际上是一个 Microsoft Word 文档，但示例 excel 文件显示的是动物图像，而不是 Microsoft Word 图像。但是如果你打开[输出excel文件](5115225.xlsx)，您将看到 Microsoft Excel 显示正确的 OLE 图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
