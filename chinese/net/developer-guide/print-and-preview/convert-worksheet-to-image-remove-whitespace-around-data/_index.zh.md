---
title: 将工作表转换为图像 - 删除数据周围的空白
type: docs
weight: 40
url: /zh/net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

有时，您需要在应用程序或网页中呈现工作表图像。例如，您可能需要将图像插入到Word文档、PDF文件、PowerPoint演示文稿或其他文档中。基本上，您希望将工作表呈现为图像，以便将其粘贴到其他应用程序中。Aspose.Cells允许您将Microsoft Excel工作表转换为图像。

{{% /alert %}}

## **删除数据周围的空白**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) API将工作表转换为带有指定属性的图像文件，例如图像格式、分页工作表等。支持多种图像格式，包括BMP、GIF、JPG、TIFF和EMF。

当使用工作表转图像功能时，默认情况下输出图像周围会有空白边框。您可以通过将源工作表的顶部、底部、左侧和右侧页面设置边距设置为0，并相应地指定[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)属性来移除此边框。

以下代码片段移除输出图像中数据周围的空白。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

