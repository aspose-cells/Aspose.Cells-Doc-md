---
title: 将工作表转换为图像  删除数据周围的空白
type: docs
weight: 40
url: /zh/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

有时，需要在应用程序或网页中显示工作表图像。例如，将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档。基本上，你希望将工作表渲染成图像，便于粘贴到其他应用中。Aspose.Cells for Python via .NET 允许你将 Microsoft Excel 工作表转换为图像。

{{% /alert %}}

## **删除数据周围的空白**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) API 可将工作表转换为带有任何指定属性（例如图像格式、分页工作表等）的图像文件。支持多种图像格式，包括 BMP、GIF、JPG、TIFF 和 EMF。

使用工作表转图像功能时，默认情况下输出图像具有周围的空白（即边框）。您可以通过将源工作表的顶部、底部、左侧和右侧的页面设置边距设置为 0，并相应地指定 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) 属性来删除这些空白。

以下代码片段删除输出图像中的数据周围的空白。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

