---
title: 将 XLSX 文件转换为 PDF 格式
type: docs
weight: 30
url: /zh/python-net/convert-xlsx-file-to-pdf-format/
description: 了解如何使用 Aspose.Cells for Python via .NET API 将 XLSX 文件转换为 PDF 格式。
keywords: Python Convert XLSX File to PDF Format, Convert xlsx to pdf using Python, Python xlsx to pdf, Save xlsx to pdf in python, xlsx to pdf format in Python
---
{{% alert color="primary" %}}

PDF（便携式文档格式）表示独立于用于创建这些文档的软件、硬件和操作系统的文档。 PDF 文件可以是具有与设备无关和分辨率无关的方式的文本、图形和图像的任意组合的文档。 PDF 文件通常被压缩，因此它们比原始文件占用更少的空间。

有时，您需要将 Microsoft Excel 文件转换为 PDF。为此，您需要一个快速、安全、准确且可靠的解决方案，让您可以在世界各地分发 PDF 文档。有许多转换工具可以执行此任务。但您必须确保原始 Excel 文档的布局保留在输出 PDF 文件中。图像、图表、形状、数据格式、字体、属性、颜色、页面设置、文本方向、边框、图表等应准确、精确地呈现。[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/)确保高保真转换。

本文档旨在全面了解如何将 Microsoft Excel 文档（包含图像、图表、格式等）转换为 PDF。为此，演示如何在 Visual Studio.Net 中创建一个简单的控制台应用程序来转换使用 Aspose.Cells for Python via .NET API 将 Excel 文件转换为 PDF。转换以高精度和准确度进行。

{{% /alert %}}

##  **将 Excel 转换为 PDF**

此示例使用 Excel 文件 (SampleInput.xlsx) 作为模板。该工作簿包含带有图表和图像的工作表。每个工作表都包含使用字体、属性、颜色、阴影效果和边框的不同类型的格式。第一个工作表上有一个柱形图，最后一个工作表上有一个图像。

###  **Excel 模板文件**

模板文件有三个工作表，包括图表和图像作为媒体。第一个工作表包含图表，最后一个工作表包含图像，如下面的屏幕截图所示。

|![待办事项：图像_替代_文本](Convert_an_XLS_File_to_PDF_Sheet1.png)|![待办事项：图像_替代_文本](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|第一个工作表**（销售预测）**|第二张工作表**（销售报告）**|
|![待办事项：图像_替代_文本](Convert_an_XLS_File_to_PDF_Sheet3.png)|![待办事项：图像_替代_文本](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|第三张工作表**（数据输入）**|最后一张工作表**（图像）**|

###  **转换过程**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好调用[工作簿.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法在将电子表格渲染到 PDF 之前。这样做可确保重新计算公式相关值，并在 PDF 中渲染正确的值。

{{% /alert %}}

###  **结果**

运行上述代码后，会在应用程序目录的 Files 文件夹中创建一个 PDF 文件。
以下屏幕截图显示了 PDF 页面。请注意，页眉和页脚也保留在输出 PDF 文件中。

|![待办事项：图像_替代_文本](Convert_an_XLS_File_to_PDF_Converted1.png)|![待办事项：图像_替代_文本](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|第一个工作表**（销售预测）**|第二张工作表**（销售报告）**|
|![待办事项：图像_替代_文本](Convert_an_XLS_File_to_PDF_Converted3.png)|![待办事项：图像_替代_文本](Convert_an_XLS_File_to_PDF_Converted4.png)|
|第三张工作表**（数据输入）**|最后一张工作表**（图像）**|
