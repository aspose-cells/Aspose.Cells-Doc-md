---
title: 将 Excel 转换为 Pdf、图像及其他格式
linktitle: 工作簿转换
type: docs
weight: 65
url: /zh/net/convert-workbook-to-different-formats/
description: 将Excel文件转换为Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XML等多种格式。
---

{{% alert color="primary" %}}

Aspose.Cells支持多种格式之间的转换。技术上，转换意味着加载一个工作簿的一个文件格式，然后将其保存为另一个文件格式。

{{% /alert %}}

## **将 Excel 工作簿转换为 PDF**

PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将Microsoft Excel文件转换为PDF文档。

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **将 Excel 工作簿转换为 JPG**
Aspose.Cells支持将Excel文件转换为JPG。
以下代码示例显示了如何将工作簿保存为JPG格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **将Excel工作簿转换为图像**
Aspose.Cells支持将Excel文件转换为图像。
以下代码示例显示了如何将工作簿保存为图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **将Excel工作簿转换为XPS**

XPS文档格式由结构化的XML标记组成，用于定义文档的布局和每个页面的视觉外观，同时还包括用于分发、归档、渲染、处理和打印文档的渲染规则。

XPS的标记语言是XAML的子集，允许在文档中包含矢量图形元素，使用XAML来标记Windows Presentation Foundation（WPF）的基元。所使用的元素是根据路径和其他几何原语来描述的。

实际上，XPS文件是一个使用开放打包约定的Unicode ZIP存档，包含构成文档的文件。这些文件包括每个页面的XML标记文件、文本、嵌入字体、光栅图像、2D矢量图形，以及数字版权管理信息。可以通过在支持ZIP文件的应用程序中打开XPS文件来查看其内容。

从Aspose.Cells 6.0.0开始，支持将Microsoft Excel转换为XPS。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **转换Excel为Ods、Sxc和Fods（OpenOffice / LibreOffice Calc）**
Aspose.Cells支持将Excel文件转换为Ods、Sxc和Fods文件。下面的代码示例显示了如何将[tempalte](book1.xlsx)转换为Ods、Sxc和Fods文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **将Excel工作簿转换为MHTML文件**

MHTML结合了普通HTML以及外部资源（通常是链接的内容，如图像、动画、音频等）到一个文件中。它们通常用于以.mht文件扩展名的电子邮件。

Aspose.Cells支持读取和写入MHTML文件。

下面的代码示例显示了如何将工作簿保存为MHTML文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **将Excel工作簿转换为HTML**

Aspose.Cells API提供对导出电子表格到HTML格式的支持。为此，Aspose.Cells使用**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**类来提供灵活性以控制输出HTML的几个方面。

下面的代码示例显示了如何将工作簿保存为HTML文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **为HTML设置图像首选项**

从8.0.2开始，Aspose.Cells公开了**[ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**，用于**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**类，允许开发人员在将电子表格保存为HTML格式时指定图像首选项。

以下是可以应用的一些图像设置的详细信息。

- **[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**: 指定图像类型。请注意，所有形状，包括图表，在输出的HTML中都被渲染为图像。
- **[SmoothingMode](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**: 指定线条，曲线和填充区域边缘的抗锯齿。
- **[TextRenderingHint](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)**: 指定文本渲染的质量。
- **[Quality](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)**: 指定图像质量在0到100之间，当**[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**指定为Jpeg时。
- **[VerticalResolution](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution) **: 获取或设置图像的垂直分辨率，单位为每英寸点数。
- **[HorizontalResolution](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution) **: 获取或设置图像的水平分辨率，单位为每英寸点数。
- **[TiffCompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression) **: 在指定**[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)** 为 Tiff 时，获取或设置图像的压缩类型。
- **[Transparent](https://reference.aspose.com/cells/net/aspose.cells/rendering/imageorprintoptions/properties/transparent) **: 当 ImageFormat 指定为 Png 时，指示图像的背景是否应为透明。

下面的代码示例演示了如何使用 **[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)** 来指定不同的偏好设置。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **将Excel工作簿转换为Markdown**

Aspose.Cells API 支持将电子表格导出为 Markdown 格式。要将活动工作表导出为 Markdown，请在 **[Workbook.Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/save/methods/3)** 的第二个参数中传递 **[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** 。您还可以使用 **[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)** 类来指定导出工作表到 Markdown 的附加设置。

下面的代码示例演示了如何使用 **[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** 枚举成员将活动工作表导出为 Markdown。请参见代码生成的[Markdown 文件](md_sample.txt)以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **将Excel工作簿转换为JSON**

Aspose.Cells支持将工作簿转换为Json（JavaScript对象表示）文件。

下面的代码示例演示了通过使用[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员将活动工作表导出为Json。请参考用于将[源文件](Book1.xlsx)转换为[输出Json文件](Book1.Json)的代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **将Excel转换为XML**
Aspose.Cells 支持将工作簿转换为 Excel 2003 电子表格 XML 和普通 XML 数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **将Excel工作簿转换为TIFF**
Aspose.Cells 支持将工作簿转换为 TIFF 文件。

下面的代码片段显示了如何将Excel转换为TIFF：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **将Excel工作簿转换为DOCX**

Aspose.Cells API 支持将电子表格转换为 DOCX 格式。要将工作簿导出到 DOCX，请将 [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) 方法的第二个参数。您还可以使用 [**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) 类来指定导出工作表到 DOCX 的附加设置。

下面的代码示例演示了通过使用[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员将活动工作表导出为DOCX。请参考代码生成的[DOCX文件](Book1.docx)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **将Excel工作簿转换为PPTX**

Aspose.Cells API 支持将电子表格转换为 PPTX 格式。要将工作簿导出到 PPTX，请将 [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) 方法的第二个参数。您还可以使用 [**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) 类来指定导出工作表到 PPTX 的附加设置。

以下代码示例演示了使用[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员将活动工作表导出到PPTX。请查看代码生成的[输出PPTX文件](Book1.pptx)作为参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **高级主题**
- [将XLSB的修订版转换为XLSM](/cells/zh/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/zh/net/convert-excel-to-html/)
- [图像](/cells/zh/net/convert-excel-to-image/)
- [Json](/cells/zh/net/convert-workbook-to-json/)
- [将Excel工作簿转换为Ods、Sxc和Fods（OpenOffice / LibreOffice calc）。](/cells/zh/net/convert-excel-to-ods/)
- [Pdf](/cells/zh/net/convert-excel-workbook-to-pdf/)
- [将Excel转换为CSV、TSV和Txt](/cells/zh/net/convert-excel-to-csv-tsv-and-txt/)
- [跟踪文档转换进度](/cells/zh/net/track-document-conversion-progress/)
- [将CSV、TSV和TXT转换为Excel](/cells/zh/net/convert-csv-tsv-and-txt-to-excel/)
