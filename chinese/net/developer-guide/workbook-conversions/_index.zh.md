---
title: 将Excel转换为Pdf、图像和其他格式
linktitle: 工作簿转换
type: docs
weight: 65
url: /zh/net/convert-workbook-to-different-formats/
description: 将Excel文件转换为Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XML等。
---

{{% alert color="primary" %}}

Aspose.Cells支持多种格式之间的转换。技术上，转换意味着以一种文件格式加载工作簿，然后将其保存为另一种格式。

{{% /alert %}}

## **将Excel工作簿转换为PDF**

PDF文件广泛用于组织、政府部门和个人之间交换文件。这是一种标准文档格式，软件开发人员经常被要求找到一种将Microsoft Excel文件转换为PDF文档的方法。

Aspose.Cells支持将Excel文件转换为PDF，并在转换中保持高视觉保真度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **将Excel工作簿转换为JPG**
Aspose.Cells支持将Excel文件转换为JPG。
下面的代码示例显示了如何将工作簿保存为JPG。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **将Excel工作簿转换为图像**
Aspose.Cells支持将Excel文件转换为图像。
下面的代码示例显示了如何将工作簿保存为图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **将Excel工作簿转换为XPS**

XPS文档格式由结构化的XML标记组成，定义文档的布局和每个页面的视觉外观，以及用于分发、存档、渲染、处理和打印文档的渲染规则。

XPS的标记语言是XAML的一个子集，允许它在文档中包含矢量图形元素，使用XAML标记Windows Presentation Foundation（WPF）的基元。使用的元素以路径和其他几何基元的形式描述。

XPS文件实际上是使用开放包装约定的Unicode ZIP存档，其中包含组成文档的文件。这些文件包括每个页面的XML标记文件、文本、嵌入式字体、栅格图像、2D矢量图形，以及数字版权管理信息。可以通过在支持ZIP文件的应用程序中简单地打开XPS文件来查看XPS文件的内容。

从Aspose.Cells 6.0.0开始，支持从Microsoft Excel转换为XPS。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **将Excel转换为Ods、Sxc和Fods（OpenOffice / LibreOffice Calc）**
Aspose.Cells支持将Excel文件转换为Ods、Sxc和Fods文件。下面的代码示例显示了如何将[模板](book1.xlsx)转换为Ods、Sxc和Fods文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **将Excel工作簿转换为MHTML文件**

MHTML将普通HTML与外部资源（通常链接的内容，如图像、动画、音频等）合并到一个文件中。它们用于扩展名为.mht的电子邮件。

Aspose.Cells支持读取和编写MHTML文件。

下面的代码示例展示了如何将工作簿保存为一个MHTML文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **将Excel工作簿转换为HTML**

Aspose.Cells API支持将电子表格导出为HTML格式。为此，Aspose.Cells使用**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**类来提供灵活性，以控制输出HTML的几个方面。

下面的代码示例显示了如何将工作簿保存为HTML文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **为HTML设置图像首选项**

从8.0.2开始，Aspose.Cells为**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**类公开了**[ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**，允许开发人员在将电子表格保存为HTML格式时指定图像首选项。

以下是一些可应用的图像设置的详细信息，

- **[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**: 指定图像类型。请注意，在输出HTML中，包括图表在内的所有形状将呈现为图像。
- **[SmoothingMode](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**: 指定线条、曲线和填充区域边缘的抗锯齿。
- **[TextRenderingHint](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)**: 指定文本呈现的质量。
- **[Quality](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)**: 在将**[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**指定为Jpeg时，指定图像的质量，范围从0到100。
- **[VerticalResolution](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)**: 获取或设置图像的垂直分辨率（每英寸点数）。
- **[HorizontalResolution](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)**: 获取或设置图像的水平分辨率（每英寸点数）。
- **[TiffCompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)**: 在**[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**指定为Tiff时，获取或设置图像的压缩类型。
- **[Transparent](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)**: 当ImageFormat指定为Png时，指示图像的背景是否应为透明。

下面的代码演示了如何使用**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**来指定不同的首选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **将Excel工作簿转换为Markdown**

Aspose.Cells API支持将电子表格导出为Markdown格式。要将活动工作表导出为Markdown，请将**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**作为**[Workbook.Save](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)**方法的第二个参数传递。您还可以使用**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)**类来指定将工作表导出为Markdown的其他设置。

以下代码示例演示了使用**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**枚举成员将活动工作表导出为Markdown。请参阅由代码生成的[输出Markdown文件](md_sample.txt)以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **将Excel工作簿转换为JSON**

Aspose.Cells支持将工作簿转换为Json（JavaScript对象表示）文件。

下面的代码示例演示了如何使用[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员将活动工作表导出为Json。 请参阅代码，以查看由代码生成的[源文件](Book1.xlsx)转换为[输出Json文件](Book1.Json)的参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **将Excel转换为XML**
Aspose.Cells支持将工作簿转换为Excel 2003电子表格XML和纯文本XML数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **将Excel工作簿转换为TIFF格式**
Aspose.Cells支持将工作簿转换为TIFF文件。

以下代码片段显示了如何将Excel转换为TIFF：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **将Excel工作簿转换为DOCX**

Aspose.Cells API提供了将电子表格转换为DOCX格式的支持。 要将工作簿导出为DOCX，请将[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)作为[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法的第二个参数传递。 您还可以使用[**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions)类指定导出工作表到DOCX的其他设置。

以下代码示例演示了如何使用[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员将活动工作表导出为DOCX。 请参阅代码，以查看由代码生成的[输出DOCX文件](Book1.docx)的参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **将Excel工作簿转换为PPTX**

Aspose.Cells API提供了将电子表格转换为PPTX格式的支持。 要将工作簿导出为PPTX，请将[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)作为[**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法的第二个参数传递。 您还可以使用[**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions)类指定导出工作表到PPTX的其他设置。

以下代码示例演示了如何使用[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员将活动工作表导出为PPTX。 请查看由代码生成的[输出PPTX文件](Book1.pptx)以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **高级主题**
- [将XLSB文件的修订版本转换为XLSM](/cells/zh/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/zh/net/convert-excel-to-html/)
- [图片](/cells/zh/net/convert-excel-to-image/)
- [Json](/cells/zh/net/convert-workbook-to-json/)
- [将Excel工作簿转换为Ods，Sxc和Fods（OpenOffice / LibreOffice Calc）。](/cells/zh/net/convert-excel-to-ods/)
- [Pdf](/cells/zh/net/convert-excel-workbook-to-pdf/)
- [将Excel转换为CSV，TSV和Txt](/cells/zh/net/convert-excel-to-csv-tsv-and-txt/)
- [跟踪文档转换进度](/cells/zh/net/track-document-conversion-progress/)
- [将CSV，TSV和TXT转换为Excel](/cells/zh/net/convert-csv-tsv-and-txt-to-excel/)
