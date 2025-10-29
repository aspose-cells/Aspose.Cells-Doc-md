---
title: 使用 C++ 通过 Golang 将 Excel 转换为 Pdf、图片等格式
linktitle: 工作簿转换
type: docs
weight: 65
url: /zh/go-cpp/convert-workbook-to-different-formats/
description: 使用Aspose.Cells for C++将Excel文件转换为Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XML等多种格式。
---

{{% alert color="primary" %}}

Aspose.Cells支持多种格式之间的转换。技术上，转换意味着加载一种文件格式的工作簿并将其保存为另一种格式。

{{% /alert %}}

## **将 Excel 工作簿转换为 PDF**

PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准的文档格式，软件开发者常被要求找到将Microsoft Excel文件转换为PDF的方法。

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions.go" >}}
## **将 Excel 工作簿转换为 JPG**
Aspose.Cells支持将Excel文件转换为JPG。
以下代码示例显示了如何将工作簿保存为JPG格式。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-1.go" >}}
## **将Excel工作簿转换为图像**
Aspose.Cells支持将Excel文件转换为图像。
以下代码示例显示了如何将工作簿保存为图像。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-2.go" >}}
## **将Excel工作簿转换为XPS**

XPS文档格式由结构化的XML标记组成，用于定义文档的布局和每个页面的视觉外观，同时还包括用于分发、归档、渲染、处理和打印文档的渲染规则。

XPS的标记语言是XAML的子集，允许在文档中加入矢量图形元素，使用XAML标记WPF基本元素。所用元素以路径和其他几何原语描述。

实际上，XPS文件是一个Unicode ZIP归档，采用开放封装规范，包含组成文档的文件。这些包括每一页的XML标记文件、文本、内嵌字体、光栅图像、二维矢量图形以及数字版权管理信息。可以通过支持ZIP文件的应用程序打开XPS文件，轻松查看其内容。

从Aspose.Cells 6.0.0开始，支持将Microsoft Excel转换为XPS。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-3.go" >}}
## **将Excel转换为Ods、Sxc和Fods（OpenOffice / LibreOffice Calc）**
Aspose.Cells支持转换Excel文件为Ods、Sxc和Fods文件。以下示例显示如何将[模板](book1.xlsx)转换为Ods、Sxc和Fods文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-4.go" >}}
## **将Excel工作簿转换为MHTML文件**

MHTML结合了普通HTML以及外部资源（通常是链接的内容，如图像、动画、音频等）到一个文件中。它们通常用于以.mht文件扩展名的电子邮件。

Aspose.Cells支持读取和写入MHTML文件。

下面的代码示例显示了如何将工作簿保存为MHTML文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-5.go" >}}
## **将Excel工作簿转换为HTML**

Aspose.Cells API 提供了导出电子表格为 HTML 格式的支持。为此，Aspose.Cells 使用 [**HtmlSaveOptions**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/) 类，提供控制输出 HTML 各个方面的灵活性。

下面的代码示例显示了如何将工作簿保存为HTML文件。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-6.go" >}}
## **为HTML设置图像首选项**

从 8.0.2 版本起，Aspose.Cells 已将 [**GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) 公开给 [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) 类，使开发者在将电子表格保存为 HTML 格式时可以指定图片偏好。

以下是一些可以应用的图像设置的详细信息：

- [**ImageType**](https://reference.aspose.com/cells/go-cpp/imagetype/)：指定图像类型。请注意，所有形状，包括图表，在输出HTML中呈现为图像。
- [**GetQuality()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getquality/)：指定当 [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) 设置为Jpeg时，图像的质量在0到100之间。
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getverticalresolution/)：获取或设置图像的垂直分辨率（每英寸点数）。
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gethorizontalresolution/)：获取或设置图像的水平分辨率（每英寸点数）。
- [**TiffCompression**](https://reference.aspose.com/cells/go-cpp/tiffcompression/)：在 [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) 被指定为 Tiff 时，获取或设置图片的压缩类型。
- [**GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/)：指示当ImageFormat指定为Png时，图像的背景是否应该是透明的。

下面的代码示例演示了如何使用[**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/)来指定不同的首选项。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-7.go" >}}
## **将Excel工作簿转换为Markdown**

Aspose.Cells API支持导出电子表格为Markdown格式。导出活动工作表为Markdown时，将 [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) 类来指定导出工作表到Markdown的其他设置。

以下示例演示如何使用 [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) 枚举成员将活动工作表导出为Markdown。请参考由代码生成的 [输出Markdown文件](md_sample.txt)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-8.go" >}}
## **将Excel工作簿转换为JSON**

Aspose.Cells支持将工作簿转换为JSON（JavaScript对象表示法）文件。

以下示例演示如何使用 [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) 枚举成员将活动工作表导出为JSON。请参阅代码示例，了解如何将 [源文件](Book1.xlsx) 转换为由代码生成的 [输出JSON文件](Book1.Json)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-9.go" >}}
## **将Excel转换为XML**
Aspose.Cells 支持将工作簿转换为 Excel 2003 电子表格 XML 和普通 XML 数据。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-10.go" >}}
## **将Excel工作簿转换为TIFF**
Aspose.Cells 支持将工作簿转换为 TIFF 文件。

下面的代码片段显示了如何将Excel转换为TIFF：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-11.go" >}}
## **将Excel工作簿转换为DOCX**

Aspose.Cells API支持将电子表格导出为DOCX格式。导出工作簿为DOCX时，将 [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) 类来指定导出到DOCX的其他设置。

以下示例演示如何使用 [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) 枚举成员将活动工作表导出为DOCX。请参考由代码生成的 [输出DOCX文件](Book1.docx)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-12.go" >}}
## **将Excel工作簿转换为PPTX**

Aspose.Cells支持将电子表格转换为PPTX格式。导出到PPTX时，将 [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) 类来指定其他导出设置。

以下示例演示如何使用 [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) 枚举成员将活动工作表导出为PPTX。请查看由代码生成的 [输出PPTX文件](Book1.pptx)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-13.go" >}}
## **将 Excel 工作簿转换为 EPUB**

Aspose.Cells API支持将电子表格转换为EPUB格式。要导出工作簿为EPUB，将 [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) 类来指定导出到EPUB的其他设置。

以下示例演示如何使用 [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) 枚举成员将活动工作表导出为EPUB。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-14.go" >}}
## **将 Excel 工作簿转换为 AZW3**

Aspose.Cells API支持将电子表格转换为AZW3格式。要导出工作簿到AZW3，传递 [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) 类指定其他导出设置。

以下示例演示如何将活动工作表导出为AZW3，使用 [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) 枚举成员。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-15.go" >}}
## **高级主题**
- [将XLSB的修订版转换为XLSM](/cells/zh/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/zh/cpp/convert-excel-to-html/)
- [图像](/cells/zh/cpp/convert-excel-to-image/)
- [Json](/cells/zh/cpp/convert-workbook-to-json/)
- [将Excel工作簿转换为Ods、Sxc和Fods（OpenOffice / LibreOffice Calc）](/cells/zh/cpp/convert-excel-to-ods/)
- [Pdf](/cells/zh/cpp/convert-excel-workbook-to-pdf/)
- [转换Excel为CSV、TSV和Txt](/cells/zh/cpp/convert-excel-to-csv-tsv-and-txt/)
- [跟踪文档转换进度](/cells/zh/cpp/track-document-conversion-progress/)
- [将CSV、TSV和TXT转换为Excel](/cells/zh/cpp/convert-csv-tsv-and-txt-to-excel/)
