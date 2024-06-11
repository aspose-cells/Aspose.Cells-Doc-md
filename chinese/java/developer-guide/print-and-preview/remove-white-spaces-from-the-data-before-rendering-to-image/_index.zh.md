---
title: 在将数据呈现为图像之前从数据中删除空白格
type: docs
weight: 270
url: /zh/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

有时候，您需要在应用程序或网页中呈现工作表图像。例如，您可能需要将图像插入到 Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档中。基本上，您想要将工作表呈现为图像，以便将其粘贴到其他应用程序中。Aspose.Cells API 允许您将 Microsoft Excel 工作表转换为图像。

{{% /alert %}}

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) 类能够将工作表转换为带有任何指定属性的图像文件，例如，图像格式、分页工作表等。支持多种图像格式，包括 BMP、GIF、JPG、TIFF 和 EMF。

在使用工作表转图像功能时，默认情况下，输出图像周围会有白色/空白空间，即边框。您可以移除此空白空间。设置源工作表的顶部、左侧、底部和右侧页面设置边距为 0 并相应地指定 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) 属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
