---
title: 将Excel转换为Pdf、图像和其他格式
linktitle: 工作簿转换
type: docs
weight: 65
url: /zh/python-net/convert-workbook-to-different-formats/
description: 将Excel文件转换为Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、 JSON、SQL、XML 等，使用 Aspose.Cells for Python via .NET API。
keywords: Python Convert Excel Workbook to PDF, Convert Excel Workbook to JPG in Python, Python Convert Excel Workbook to Image, Converting Excel Workbook to XPS using Python, Convert Excel to Ods,Sxc and Fods via Python, Python Convert Excel Workbook to HTML, Convert Excel Workbook to JSON in Python, Python Convert Excel Workbook to DOCX, Convert Excel Workbook to TIFF or MARKDOWN with Ptyhon.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 支持多种格式之间的转换。从技术上讲，转换意味着加载一种文件格式的工作簿并将其保存为另一种文件格式。

{{% /alert %}}

##  **将 Excel 工作簿转换为 PDF**

PDF 文件广泛用于组织、政府部门和个人之间交换文件。它是一种标准文档格式，软件开发人员经常被要求找到一种将 Microsoft Excel 文件转换为 PDF 文档的方法。

Aspose.Cells for Python via .NET 支持将Excel文件转换为PDF，并在转换中保持高视觉保真度。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-PDF.py" >}}

##  **将 Excel 工作簿转换为 JPG**
Aspose.Cells for Python via .NET 支持将Excel文件转换为JPG。
下面的代码示例展示了如何将工作簿另存为 JPG。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JPG.py" >}}

##  **将 Excel 工作簿转换为图像**
Aspose.Cells for Python via .NET 支持将Excel文件转换为图像。
下面的代码示例展示了如何将工作簿另存为图像。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Image.py" >}}

##  **将 Excel 工作簿转换为 XPS**

XPS 文档格式由结构化 XML 标记组成，该标记定义文档的布局和每个页面的视觉外观，以及用于分发、存档、呈现、处理和打印文档的呈现规则。

XPS 的标记语言是 XAML 的子集，它允许它在文档中合并矢量图形元素，使用 XAML 来标记 Windows 演示基础 (WPF) 原语。使用的元素是根据路径和其他几何图元来描述的。

事实上，XPS 文件是使用开放打包约定的 unicode ZIP 存档，包含构成该文档的文件。其中包括每个页面的 XML 标记文件、文本、嵌入字体、光栅图像、2D 矢量图形以及数字版权管理信息。只需在支持 ZIP 文件的应用程序中打开 XPS 文件的内容即可对其进行检查。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XPS.py" >}}

##  **将 Excel 转换为 Ods、Sxc 和 Fods (OpenOffice / LibreOffice Calc)**
 Aspose.Cells for Python via .NET 支持将Excel文件转换为Ods、Sxc和Fods文件。下面的代码示例展示了如何转换[坦帕尔特](book1.xlsx)到 Ods、Sxc 和 Fods 文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-ODS.py" >}}


##  **将 Excel 工作簿转换为 MHTML 文件**

MHTML 将普通 HTML 与外部资源（即通常链接的内容，如图像、动画、音频等）合并到一个文件中。它们用于带有 .mht 文件扩展名的电子邮件。

Aspose.Cells for Python via .NET 支持读写 MHTML 文件。

下面的代码示例显示如何将工作簿另存为 MHTML 文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-MHTML.py" >}}

##  **将 Excel 工作簿转换为 HTML**

 Aspose.Cells for Python via .NET API 支持将电子表格导出为 HTML 格式。为此，Aspose.Cells for Python via .NET 使用**[HtmlSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/)**类提供了控制输出HTML的几个方面的灵活性。

下面的代码示例显示如何将工作簿另存为 HTML 文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML.py" >}}

##  **设置 HTML 的图像首选项**

Aspose.Cells for Python via .NET 已曝光**[图像选项](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/)**为了**[HtmlSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions)**类，允许开发人员在将电子表格保存为 HTML 格式时指定图像首选项。

以下是一些可以应用的图像设置的详细信息，

- *[图像类型](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)**：指定图像类型。请注意，所有形状（包括图表）都会在输出 HTML 中呈现为图像。
- *[平滑模式](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/smoothing_mode/)**：指定填充区域的直线、曲线和边缘的抗锯齿。
- *[文本渲染提示](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/text_rendering_hint/)**：指定文本渲染的质量。
- **[quality](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/quality/)**：指定图像的质量在0到100之间，当**[ImageType ](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)**指定为 Jpeg。
- *[垂直分辨率](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)**：获取或设置图像的垂直分辨率（以每英寸点数为单位）。
- *[水平分辨率](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/)**：获取或设置图像的水平分辨率（以每英寸点数为单位）。
- **[tiff_compression](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/)**：获取或设置图像的压缩类型**[ImageType]( https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/）**指定为 Tiff。
- *[透明的](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent/)**：指示当 ImageFormat 指定为 Png 时图像背景是否应透明。

下面的代码演示了如何使用**[HtmlSaveOptions.image_options](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/)**指定不同的首选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML-SettingImagePrefrencesforHTML-1.py" >}}

##  **将 Excel 工作簿转换为 Markdown**

Aspose.Cells for Python via .NET API 支持将电子表格导出为 Markdown 格式。要将活动工作表导出到 Markdown，请传递**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**作为第二个参数**[工作簿.保存](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)**方法。您还可以使用**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)**类指定将工作表导出到 Markdown 的其他设置。

以下代码示例演示了使用以下命令将活动工作表导出到 Markdown**[SaveFormat.MARKDOWN](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**枚举成员。请参阅[输出 Markdown 文件](md_sample.txt)代码生成，供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Markdown-1.py" >}}

##  **将 Excel 工作簿转换为 JSON**

Aspose.Cells for Python via .NET 支持将工作簿转换为 Json(JavaScript Object Notation) 文件。

以下代码示例演示了使用以下方法将活动工作表导出为 Json[**保存格式.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员。请参阅要转换的代码[源文件](Book1.xlsx)到[输出Json文件](Book1.Json)代码生成，供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

##  **将 Excel 转换为 XML**
Aspose.Cells for Python via .NET 支持将工作簿转换为 Excel 2003 电子表格 XML 和纯 XML 数据。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XML.py" >}}

##  **将 Excel 工作簿转换为 TIFF**
Aspose.Cells for Python via .NET 支持将工作簿转换为 TIFF 文件。

下面的代码片段显示了如何将 Excel 转换为 TIFF：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-TIFF.py" >}}

##  **将 Excel 工作簿转换为 DOCX**

Aspose.Cells for Python via .NET API 支持将电子表格转换为 DOCX 格式。要将工作簿导出到 DOCX，请通过[**保存格式.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)作为第二个参数[**工作簿.保存**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions)方法。您还可以使用[**Docx保存选项**](https://reference.aspose.com/cells/python-net/aspose.cells/docxsaveoptions/)类指定将工作表导出到 DOCX 的其他设置。

以下代码示例演示了使用以下命令将活动工作表导出到 DOCX[**保存格式.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员。请参阅[输出DOCX文件](Book1.docx)代码生成，供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Docx-1.py" >}}

##  **将 Excel 工作簿转换为 PPTX**

Aspose.Cells for Python via .NET API 支持将电子表格转换为 PPTX 格式。要将工作簿导出到 PPTX，请通过[**保存格式.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)作为第二个参数[**工作簿.保存**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions)方法。您还可以使用[**Pptx保存选项**](https://reference.aspose.com/cells/python-net/aspose.cells/pptxsaveoptions)类指定将工作表导出到 PPTX 的其他设置。

以下代码示例演示了使用以下命令将活动工作表导出到 PPTX[**保存格式.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员。请参阅[输出PPTX文件](Book1.pptx)代码生成，供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-File-To-Pptx-1.py" >}}

##  **高级主题**
- [杰森](/cells/zh/python-net/convert-workbook-to-json/)
- [pdf](/cells/zh/python-net/convert-excel-to-pdf/)
- [将 CSV、TSV 和 TXT 转换为 Excel](/cells/zh/python-net/convert-csv-tsv-and-txt-to-excel/)
