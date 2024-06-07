---
title: 将Excel转换为Pdf、图像和其他格式
linktitle: 工作簿转换
type: docs
weight: 65
url: /zh/python-net/convert-workbook-to-different-formats/
description: 通过使用Aspose.Cells for Python通过.NET API，将Excel文件转换为Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XML等更多格式。
keywords: Python将Excel工作簿转换为PDF，在Python中将Excel工作簿转换为JPG，Python中将Excel工作簿转换为图像，使用Python将Excel工作簿转换为XPS，在Python中将Excel转换为Ods、Sxc和Fods，Python中将Excel工作簿转换为HTML，使用Python将Excel工作簿转换为JSON，在Python中将Excel工作簿转换为DOCX，使用Python将Excel工作簿转换为TIFF或MARKDOWN。
---

{{% alert color="primary" %}}

Aspose.Cells for Python通过.NET支持许多格式之间的转换。从技术上讲，转换意味着在一个文件格式中加载工作簿并将其保存到另一个文件格式中。

{{% /alert %}}

## **将Excel工作簿转换为PDF**

PDF文件广泛用于组织、政府部门和个人之间交换文件。这是一种标准文档格式，软件开发人员经常被要求找到一种将Microsoft Excel文件转换为PDF文档的方法。

Aspose.Cells for Python通过.NET支持将Excel文件转换为PDF，并且在转换过程中保持高度视觉保真度。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-PDF.py" >}}

## **将Excel工作簿转换为JPG**
Aspose.Cells for Python通过.NET支持将Excel文件转换为JPG。
下面的代码示例显示了如何将工作簿保存为JPG。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JPG.py" >}}

## **将Excel工作簿转换为图像**
Aspose.Cells for Python通过.NET支持将Excel文件转换为图像。
下面的代码示例显示了如何将工作簿保存为图像。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Image.py" >}}

## **将Excel工作簿转换为XPS**

XPS文档格式由结构化的XML标记组成，定义文档的布局和每个页面的视觉外观，以及用于分发、存档、渲染、处理和打印文档的渲染规则。

XPS的标记语言是XAML的一个子集，允许它在文档中包含矢量图形元素，使用XAML标记Windows Presentation Foundation（WPF）的基元。使用的元素以路径和其他几何基元的形式描述。

XPS文件实际上是使用开放包装约定的Unicode ZIP存档，其中包含组成文档的文件。这些文件包括每个页面的XML标记文件、文本、嵌入式字体、栅格图像、2D矢量图形，以及数字版权管理信息。可以通过在支持ZIP文件的应用程序中简单地打开XPS文件来查看XPS文件的内容。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XPS.py" >}}

## **将Excel转换为Ods、Sxc和Fods（OpenOffice / LibreOffice Calc）**
Aspose.Cells for Python通过.NET支持将Excel文件转换为Ods、Sxc和Fods文件。下面的代码示例显示了如何将[模板](book1.xlsx)转换为Ods、Sxc和Fods文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-ODS.py" >}}


## **将Excel工作簿转换为MHTML文件**

MHTML将普通HTML与外部资源（通常链接的内容，如图像、动画、音频等）合并到一个文件中。它们用于扩展名为.mht的电子邮件。

Aspose.Cells for Python通过.NET支持读写MHTML文件。

下面的代码示例展示了如何将工作簿保存为一个MHTML文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-MHTML.py" >}}

## **将Excel工作簿转换为HTML**

Aspose.Cells for Python通过.NET API支持将电子表格导出为HTML格式。为此，Aspose.Cells for Python通过.NET使用**[HtmlSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/)**类提供了灵活性，以控制输出HTML的几个方面。

下面的代码示例显示了如何将工作簿保存为HTML文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML.py" >}}

## **为HTML设置图像首选项**

Aspose.Cells for Python通过.NET公开了**[image_options](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/)**作为**[HtmlSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions)**类的一部分，允许开发人员在将电子表格保存为HTML格式时指定图像偏好设置。

以下是一些可应用的图像设置的详细信息，

- **[ImageType](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)**：指定图像类型。请注意，所有形状，包括图表，在输出HTML中呈现为图像。
- **[smoothing_mode](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/smoothing_mode/)**：指定线条、曲线和填充区域的反锯齿。
- **[text_rendering_hint](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/text_rendering_hint/)**：指定文本渲染的质量。
- **[quality](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/quality/)**：在指定**[ImageType](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)**为Jpeg时，指定图像质量在0到100之间。
- **[vertical_resolution](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)**：设置图像的垂直分辨率，单位为每英寸点数。
- **[horizontal_resolution](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/)**：设置图像的水平分辨率，单位为每英寸点数。
- **[tiff_compression](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/)**：在指定**[ImageType](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)** 为Tiff时，获取或设置图像的压缩类型。
- **[transparent](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent/)**：指示在ImageFormat指定为Png时，图像的背景是否应该是透明的。

下面的代码示例演示了如何使用**[HtmlSaveOptions.image_options](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/)**指定不同的偏好设置。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML-SettingImagePrefrencesforHTML-1.py" >}}

## **将Excel工作簿转换为Markdown**

Aspose.Cells for Python通过.NET API支持将电子表格导出为Markdown格式。要将活动工作表导出为Markdown，请将**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**作为**[Workbook.Save](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)**方法的第二个参数传递。您也可以使用**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)**类指定导出工作表为Markdown的其他设置。

以下代码示例演示了如何使用**[SaveFormat.MARKDOWN](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**枚举成员将活动工作表导出为Markdown。 请参阅代码生成的参考的[输出Markdown文件](md_sample.txt)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Markdown-1.py" >}}

## **将Excel工作簿转换为JSON**

Aspose.Cells for Python通过.NET支持将工作簿转换为Json（JavaScript对象表示）文件。

下面的代码示例演示了如何使用[**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员将活动工作表导出为Json。 请参阅代码，以查看由代码生成的[源文件](Book1.xlsx)转换为[输出Json文件](Book1.Json)的参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

## **将Excel转换为XML**
Aspose.Cells for Python通过.NET支持将工作簿转换为Excel 2003电子表格XML和纯XML数据。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XML.py" >}}

## **将Excel工作簿转换为TIFF格式**
Aspose.Cells for Python通过.NET支持将工作簿转换为TIFF文件。

以下代码片段显示了如何将Excel转换为TIFF：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-TIFF.py" >}}

## **将Excel工作簿转换为DOCX**

Aspose.Cells for Python通过.NET API支持将电子表格转换为DOCX格式。要导出工作簿到DOCX，请将[**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)作为[**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions)方法的第二个参数。您还可以使用[**DocxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/docxsaveoptions/)类来指定导出工作表到DOCX的其他设置。

以下代码示例演示了如何使用[**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员将活动工作表导出为DOCX。 请参阅代码，以查看由代码生成的[输出DOCX文件](Book1.docx)的参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Docx-1.py" >}}

## **将Excel工作簿转换为PPTX**

Aspose.Cells for Python通过.NET API支持将电子表格转换为PPTX格式。要导出工作簿到PPTX，请将[**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)作为[**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions)方法的第二个参数。您还可以使用[**PptxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pptxsaveoptions)类来指定导出工作表到PPTX的其他设置。

以下代码示例演示了如何使用[**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员将活动工作表导出为PPTX。 请查看由代码生成的[输出PPTX文件](Book1.pptx)以供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-File-To-Pptx-1.py" >}}

## **高级主题**
- [Json](/cells/zh/python-net/convert-workbook-to-json/)
- [Pdf](/cells/zh/python-net/convert-excel-to-pdf/)
- [将CSV，TSV和TXT转换为Excel](/cells/zh/python-net/convert-csv-tsv-and-txt-to-excel/)
