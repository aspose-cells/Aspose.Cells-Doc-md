---
title: 将工作表转换为图像 - 删除数据周围的空白
type: docs
weight: 40
url: /zh/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

有时，您需要在应用程序或网页中显示工作表图像。例如，您可能需要将图像插入到 Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档中。基本上，您希望将工作表呈现为图像，以便可以将其粘贴到其他应用程序中。 Aspose.Cells 允许您将 Microsoft Excel 工作表转换为图像。

{{% /alert %}}

## **删除数据周围的空白**

这[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API 将工作表转换为具有任意指定属性的图像文件，例如图像格式、分页纸等。支持多种图像格式，包括 BMP、GIF、JPG、TIFF 和 EMF。

当您使用图纸到图像功能时，默认情况下输出图像周围有空白，即边框。您可以通过将源工作表的顶部、底部、左侧和右侧页面设置页边距设置为 0 来删除它，并指定[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)相应的属性。

以下代码片段删除了输出图像中数据周围的空白。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

