---
title: 将工作表转换为图像  删除数据周围的空白
type: docs
weight: 40
url: /zh/net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

有时，您需要在应用程序或网页中呈现工作表图像。例如，您可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档中。基本上，您希望将工作表呈现为图像，以便将其粘贴到其他应用程序中。Aspose.Cells 允许您将 Microsoft Excel 工作表转换为图像。

{{% /alert %}}

## **删除数据周围的空白**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) API 可将工作表转换为带有任何指定属性（例如图像格式、分页工作表等）的图像文件。支持多种图像格式，包括 BMP、GIF、JPG、TIFF 和 EMF。

使用工作表转图像功能时，默认情况下输出图像具有周围的空白（即边框）。您可以通过将源工作表的顶部、底部、左侧和右侧的页面设置边距设置为 0，并相应地指定 [**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) 属性来删除这些空白。

以下代码片段删除输出图像中的数据周围的空白。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
