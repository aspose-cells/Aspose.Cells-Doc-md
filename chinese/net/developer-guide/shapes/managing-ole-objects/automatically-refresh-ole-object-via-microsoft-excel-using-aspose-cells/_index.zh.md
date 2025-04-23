---
title: 使用Aspose.Cells自动刷新OLE对象通过Microsoft Excel
type: docs
weight: 270
url: /zh/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells提供 [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) 属性，在Microsoft Excel中打开excel文件时刷新OLE对象。由于该属性，OLE对象将显示由Microsoft Excel生成的正确OLE图像。

{{% /alert %}}

以下样本代码加载了包含非真实OLE图像的 [样本excel文件](5115231.xlsx)。OLE对象实际上是一个Microsoft Word文档，但样本excel文件显示的是动物图像，而不是Microsoft Word图像。但是，如果打开 [输出excel文件](5115225.xlsx)，您将看到Microsoft Excel显示了正确的OLE图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
