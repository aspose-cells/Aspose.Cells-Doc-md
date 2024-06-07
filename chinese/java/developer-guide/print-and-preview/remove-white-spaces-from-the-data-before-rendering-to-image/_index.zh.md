---
title: 在渲染图像之前从数据中删除空格
type: docs
weight: 270
url: /zh/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

有时，您需要在应用程序或网页中展示工作表图像。例如，您可能需要将图像插入到Word文档、PDF文件、PowerPoint演示文稿或其他文档中。基本上，您希望将工作表渲染为图像，以便可以粘贴到其他应用程序中。Aspose.Cells API允许您将Microsoft Excel工作表转换为图像。

{{% /alert %}}

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)类能够将工作表转换为具有任何指定属性的图像文件，例如图像格式、分页工作表等。支持多种图像格式，包括BMP、GIF、JPG、TIFF和EMF。

当您使用表格转图像功能时，默认情况下输出图像周围有白色/空白空间，即边框。您可以将其删除。将源工作表的顶部、左侧、底部和右侧页面设置边距设置为0，并相应地指定[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
