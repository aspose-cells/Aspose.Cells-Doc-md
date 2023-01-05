---
title: Excel转Pdf、图片等格式
linktitle: 工作簿转换
type: docs
weight: 65
url: /zh/net/convert-workbook-to-different-formats/
description: 将 Excel 文件转换为 Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、0761934611、TIFF、0761934611、07 更多 XML
---
{{% alert color="primary" %}}

Aspose.Cells 支持多种格式之间的转换。从技术上讲，转换意味着以一种文件格式加载工作簿并将其保存为另一种文件格式。

{{% /alert %}}

## **将 Excel 工作簿转换为 PDF**

PDF 文件广泛用于组织、政府部门和个人之间交换文件。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将 Microsoft Excel 文件转换为 PDF 文档。

Aspose.Cells 支持将 Excel 文件转换为 PDF，并在转换中保持高视觉保真度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **将 Excel 工作簿转换为 JPG**
Aspose.Cells 支持将Excel文件转换为JPG。
下面的代码示例显示了如何将工作簿另存为 JPG。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **将 Excel 工作簿转换为图像**
Aspose.Cells 支持Excel文件转图片。
下面的代码示例显示了如何将工作簿另存为图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **将 Excel 工作簿转换为 XPS**

XPS 文档格式包含定义文档布局和每个页面的视觉外观的结构化 XML 标记，以及用于分发、存档、呈现、处理和打印文档的呈现规则。

XPS 的标记语言是 XAML 的一个子集，它允许它在文档中合并矢量图形元素，使用 XAML 标记 Windows Presentation Foundation (WPF) 原语。使用的元素根据路径和其他几何图元进行描述。

XPS 文件实际上是一个使用开放打包约定的 unicode ZIP 存档，其中包含构成文档的文件。其中包括每个页面的 XML 标记文件、文本、嵌入字体、光栅图像、2D 矢量图形以及数字版权管理信息。只需在支持 ZIP 文件的应用程序中将其打开，即可检查 XPS 文件的内容。

从 Aspose.Cells 6.0.0，支持 Microsoft Excel 到 XPS 的转换。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **将 Excel 转换为 Ods、Sxc 和 Fods（OpenOffice / LibreOffice Calc）**
 Aspose.Cells 支持将Excel文件转换为Ods、Sxc和Fods文件。下面的代码示例显示了如何将[模板](book1.xlsx)到 Ods、Sxc 和 Fods 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **将 Excel 工作簿转换为 MHTML 文件**

MHTML 将正常的 HTML 与外部资源（即通常链接进来的内容，如图像、动画、音频等）合并到一个文件中。它们用于文件扩展名为 .mht 的电子邮件。

Aspose.Cells支持读写MHTML文件。

下面的代码示例显示了如何将工作簿另存为 MHTML 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **将 Excel 工作簿转换为 HTML**

 Aspose.Cells API 提供了将电子表格导出为HTML格式的支持。为此，Aspose.Cells 使用**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**类提供灵活性来控制输出 HTML 的几个方面。

下面的代码示例显示了如何将工作簿另存为 HTML 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **为 HTML 设置图像首选项**

从8.0.2开始，Aspose.Cells暴露了**[图像选项](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**为了**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**类，允许开发人员在将电子表格保存为 HTML 格式时指定图像首选项。

以下是一些可以应用的图像设置的详细信息，

- **[图像类型](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**：指定图像类型。请注意，所有形状（包括图表）在输出 HTML 中呈现为图像。
- **[平滑模式](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**：指定填充区域的直线、曲线和边缘的抗锯齿。
- **[TextRenderingHint](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)**：指定文本呈现的质量。
- **[质量](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)** ：指定图像的质量在 0 到 100 之间，当**[图像类型](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**指定为 Jpeg。
- **[垂直分辨率](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)**: 获取或设置图像的垂直分辨率（以每英寸点数为单位）。
- **[水平分辨率](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)**获取或设置图像的水平分辨率（以每英寸点数为单位）。
- **[TiffCompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)** : 获取或设置图片压缩类型**[图像类型](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**指定为 Tiff。
- **[透明](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)**: 指示当 ImageFormat 指定为 Png 时图像的背景是否应该透明。

下面的代码演示了如何使用**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**指定不同的首选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **将 Excel 工作簿转换为 Markdown**

Aspose.Cells API 提供了将电子表格导出为Markdown格式的支持。要将活动工作表导出到 Markdown，请通过**[保存格式.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**作为第二个参数**[工作簿.保存](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)**方法。您也可以使用**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)**类以指定将工作表导出到 Markdown 的其他设置。

下面的代码示例演示了通过使用将活动工作表导出到 Markdown**[保存格式.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**枚举成员。请参阅[输出 Markdown 文件](md_sample.txt)生成的代码供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **将 Excel 工作簿转换为 JSON**

Aspose.Cells 支持将工作簿转换为 Json（JavaScript Object Notation）文件。

下面的代码示例演示了通过使用将活动工作表导出到 Json[**保存格式.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员。请看代码转换[源文件](Book1.xlsx)到[输出Json文件](Book1.Json)生成的代码供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **将 Excel 转换为 XML**
Aspose.Cells 支持将工作簿转换为 Excel 2003 电子表格 XML 和纯 XML 数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **将 Excel 工作簿转换为 TIFF**
Aspose.Cells 支持将工作簿转换为 TIFF 文件。

下面的代码片段显示了如何将 Excel 转换为 TIFF：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **将 Excel 工作簿转换为 DOCX**

Aspose.Cells API 提供将电子表格转换为 DOCX 格式的支持。要将工作簿导出到 DOCX，请通过[**保存格式.docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)作为第二个参数[**工作簿.保存**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法。您也可以使用[**DocxSave选项**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions)类以指定将工作表导出到 DOCX 的其他设置。

下面的代码示例演示了通过使用将活动工作表导出到 DOCX[**保存格式.docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员。请参阅[输出 DOCX 文件](Book1.docx)生成的代码供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **将 Excel 工作簿转换为 PPTX**

Aspose.Cells API 提供将电子表格转换为 PPTX 格式的支持。要将工作簿导出到 PPTX，请通过[**保存格式.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)作为第二个参数[**工作簿.保存**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)方法。您也可以使用[**PptxSave选项**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions)类以指定将工作表导出到 PPTX 的其他设置。

下面的代码示例演示了通过使用将活动工作表导出到 PPTX[**保存格式.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员。请参阅[输出 PPTX 文件](Book1.pptx)生成的代码供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **推进主题**
- [将 XLSB 的修订版转换为 XLSM](/cells/zh/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/zh/net/convert-excel-to-html/)
- [图片](/cells/zh/net/convert-excel-to-image/)
- [杰森](/cells/zh/net/convert-workbook-to-json/)
- [将 Excel 工作簿转换为 Ods、Sxc 和 Fods (OpenOffice / LibreOffice calc)。](/cells/zh/net/convert-excel-to-ods/)
- [PDF格式](/cells/zh/net/convert-excel-workbook-to-pdf/)
- [将 Excel 转换为 CSV,TSV 和 Txt](/cells/zh/net/convert-excel-to-csv-tsv-and-txt/)
- [跟踪文档转换进度](/cells/zh/net/track-document-conversion-progress/)
- [将 CSV、TSV 和 TXT 转换为 Excel](/cells/zh/net/convert-csv-tsv-and-txt-to-excel/)
