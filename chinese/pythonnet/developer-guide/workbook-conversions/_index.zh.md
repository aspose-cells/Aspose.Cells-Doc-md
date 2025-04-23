---
title: 将 Excel 转换为 Pdf、图像及其他格式
linktitle: 工作簿转换
type: docs
weight: 65
url: /zh/python-net/convert-workbook-to-different-formats/
description: 使用 Aspose.Cells for Python via .NET API，将 Excel 文件转换为 Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XML 等格式。
keywords: Python 将 Excel 工作簿转换为 PDF，在 Python 中将 Excel 工作簿转换为 JPG，Python 将 Excel 工作簿转换为图像，使用 Python 将 Excel 工作簿转换为 XPS，使用 Python 将 Excel 转换为 ODS、SXC 和 FODS，Python 将 Excel 工作簿转换为 HTML，在 Python 中将 Excel 工作簿转换为 JSON，Python 将 Excel 工作簿转换为 DOCX，使用 Python 将 Excel 工作簿转换为 TIFF 或 MARKDOWN。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 支持多种格式之间的转换。技术上，转换意味着将一个文件格式的工作簿加载并保存为另一种格式。

{{% /alert %}}

## **将 Excel 工作簿转换为 PDF**

PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将Microsoft Excel文件转换为PDF文档。

Aspose.Cells for Python via .NET 支持将 Excel 文件转换为 PDF，并在转换中保持高视觉保真度。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-PDF.py" >}}

## **将 Excel 工作簿转换为 JPG**
Aspose.Cells for Python via .NET 支持将 Excel 文件转换为 JPG。
以下代码示例显示了如何将工作簿保存为JPG格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JPG.py" >}}

## **将Excel工作簿转换为图像**
Aspose.Cells for Python via .NET支持将Excel文件转换为图像。
以下代码示例显示了如何将工作簿保存为图像。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Image.py" >}}

## **将Excel工作簿转换为XPS**

XPS文档格式由结构化的XML标记组成，用于定义文档的布局和每个页面的视觉外观，同时还包括用于分发、归档、渲染、处理和打印文档的渲染规则。

XPS的标记语言是XAML的子集，允许在文档中包含矢量图形元素，使用XAML来标记Windows Presentation Foundation（WPF）的基元。所使用的元素是根据路径和其他几何原语来描述的。

实际上，XPS文件是一个使用开放打包约定的Unicode ZIP存档，包含构成文档的文件。这些文件包括每个页面的XML标记文件、文本、嵌入字体、光栅图像、2D矢量图形，以及数字版权管理信息。可以通过在支持ZIP文件的应用程序中打开XPS文件来查看其内容。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XPS.py" >}}

## **转换Excel为Ods、Sxc和Fods（OpenOffice / LibreOffice Calc）**
Aspose.Cells for Python via .NET支持将Excel文件转换为Ods、Sxc和Fods文件。下面的代码示例显示了如何将[模板]（book1.xlsx）转换为Ods、Sxc和Fods文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-ODS.py" >}}


## **将Excel工作簿转换为MHTML文件**

MHTML结合了普通HTML以及外部资源（通常是链接的内容，如图像、动画、音频等）到一个文件中。它们通常用于以.mht文件扩展名的电子邮件。

Aspose.Cells for Python via .NET支持读取和写入MHTML文件。下面的代码示例显示了如何将工作簿保存为MHTML文件。

下面的代码示例显示了如何将工作簿保存为MHTML文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-MHTML.py" >}}

## **将Excel工作簿转换为HTML**

Aspose.Cells for Python via .NET API支持将电子表格导出为HTML格式。为此，Aspose.Cells for Python via .NET使用[**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/)类，提供灵活性来控制输出HTML的几个方面。

下面的代码示例显示了如何将工作簿保存为HTML文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML.py" >}}

## **为HTML设置图像首选项**

Aspose.Cells for Python via .NET已为[**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions) 类公开了[**image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/)，允许开发人员在将电子表格保存为HTML格式时指定图像首选项。

以下是可以应用的一些图像设置的详细信息。

- [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)：指定图像类型。请注意，所有形状，包括图表，在输出HTML中呈现为图像。
- [**smoothing_mode**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/smoothing_mode/)：指定线条，曲线和填充区域边缘的抗锯齿。
- [**text_rendering_hint**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/text_rendering_hint/)：指定文本呈现的质量。
- [**quality**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/quality/)：在指定Jpeg时，指定图像质量为0到100之间的值。
- [**vertical_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)：获取或设置图像的垂直分辨率（每英寸点数）。
- [**horizontal_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/)：获取或设置图像的水平分辨率（每英寸点数）。
- [**tiff_compression**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/)：在指定Tiff时，获取或设置图像的压缩类型。
- [**transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent/)：指示当ImageFormat指定为Png时，图像的背景是否应该是透明的。

下面的代码示例演示了如何使用[**HtmlSaveOptions.image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) 指定不同的首选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML-SettingImagePrefrencesforHTML-1.py" >}}

## **将Excel工作簿转换为Markdown**

Aspose.Cells for Python via .NET API支持将电子表格导出为Markdown格式。要将活动工作表导出为Markdown，请将[**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)作为[**Workbook.Save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.saveformat)方法的第二个参数传递。您还可以使用[**MarkdownSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/markdownsaveoptions)类来指定导出工作表到Markdown的其他设置。

以下代码示例演示了如何通过使用[**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员将活动工作表导出为Markdown。请参考由该代码生成的[输出Markdown文件](md_sample.txt)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Markdown-1.py" >}}

## **将Excel工作簿转换为JSON**

Aspose.Cells for Python via .NET支持将工作簿转换为Json(JavaScript Object Notation)文件。

下面的代码示例演示了通过使用[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员将活动工作表导出为Json。请参考用于将[源文件](Book1.xlsx)转换为[输出Json文件](Book1.Json)的代码。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

## **将Excel转换为XML**
Aspose.Cells for Python via .NET支持将工作簿转换为Excel 2003电子表格XML和普通XML数据。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XML.py" >}}

## **将Excel工作簿转换为TIFF**
Aspose.Cells for Python via .NET支持将工作簿转换为TIFF文件。

下面的代码片段显示了如何将Excel转换为TIFF：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-TIFF.py" >}}

## **将Excel工作簿转换为DOCX**

Aspose.Cells for Python via .NET API支持将电子表格转换为DOCX格式。要将工作簿导出为DOCX，请将[**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)作为[**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions)方法的第二个参数。您还可以使用[**DocxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/docxsaveoptions/)类来指定导出工作表到DOCX的附加设置。

下面的代码示例演示了通过使用[**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员将活动工作表导出为DOCX。请参考代码生成的[DOCX文件](Book1.docx)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Docx-1.py" >}}

## **将Excel工作簿转换为PPTX**

Aspose.Cells for Python via .NET API提供了将电子表格转换为PPTX格式的支持。要将工作簿导出为PPTX，请将[**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)作为[**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions)方法的第二个参数传递。您还可以使用[**PptxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pptxsaveoptions)类来指定导出工作表到PPTX的其他设置。

以下代码示例演示了使用[**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员将活动工作表导出到PPTX。请查看代码生成的[输出PPTX文件](Book1.pptx)作为参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-File-To-Pptx-1.py" >}}

## **高级主题**
- [Json](/cells/zh/python-net/convert-workbook-to-json/)
- [Pdf](/cells/zh/python-net/convert-excel-to-pdf/)
- [将CSV、TSV和TXT转换为Excel](/cells/zh/python-net/convert-csv-tsv-and-txt-to-excel/)
