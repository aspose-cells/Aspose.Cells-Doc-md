---
title: 自动刷新 OLE 对象
type: docs
weight: 270
url: /zh/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 提供了 [**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load) 属性，在打开 Excel 文件时刷新 OLE 对象。由于该属性，OLE 对象将显示由 Microsoft Excel 生成的正确 OLE 图像。

{{% /alert %}}

以下样本代码加载了包含非真实OLE图像的 [样本excel文件](5115231.xlsx)。OLE对象实际上是一个Microsoft Word文档，但样本excel文件显示的是动物图像，而不是Microsoft Word图像。但是，如果打开 [输出excel文件](5115225.xlsx)，您将看到Microsoft Excel显示了正确的OLE图像。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
