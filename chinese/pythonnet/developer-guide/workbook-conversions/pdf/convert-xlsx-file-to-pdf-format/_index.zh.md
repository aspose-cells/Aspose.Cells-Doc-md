---
title: 将XLSX文件转换为PDF格式
type: docs
weight: 30
url: /zh/python-net/convert-xlsx-file-to-pdf-format/
description: 了解如何使用Aspose.Cells for Python通过.NET API将XLSX文件转换为PDF格式
keywords: Python将XLSX文件转换为PDF格式，在Python中使用python将xlsx转换为pdf，Python xlsx转为pdf，在python中保存xlsx到pdf，Python中的xlsx转pdf格式
---

{{% alert color="primary" %}}

PDF（便携式文档格式）代表独立于用于创建这些文档的软件、硬件和操作系统的文档。PDF文件可以以与设备无关和分辨率无关的方式包含文本、图形和图像的文档。PDF文件通常是经过压缩的，因此占用的空间比原始文件少。

有时，您需要将 Microsoft Excel 文件转换为 PDF。为此，您需要一种快速、安全、准确且可靠的解决方案，可以让您在全球范围内分发 PDF 文档。有许多转换工具可以执行此任务。但您必须确保原始 Excel 文档的布局在输出 PDF 文件中得以保留。图像、图表、形状、数据格式、字体、属性、颜色、页面设置、文本方向、边框、图表等应被准确地渲染。[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) 可确保高保真度转换。

本文档旨在全面了解如何将 Microsoft Excel 文档（包含图像、图表、格式等）转换为 PDF。为此，它演示了如何在 Visual Studio.Net 中创建一个简单的控制台应用程序，利用 Aspose.Cells for Python via .NET API 将 Excel 文件转换为 PDF。转换过程具有高度的精确度和准确性。

{{% /alert %}}

## **将Excel转换为PDF**

此示例使用Excel文件（SampleInput.xlsx）作为模板。工作簿包含具有图表和图像的工作表。每个工作表包含使用字体、属性、颜色、阴影效果和边框的不同类型格式。第一个工作表上有一个柱状图，最后一个工作表上有一张图片。

### **模板Excel文件**

模板文件包含三个工作表，包括图表和图像作为媒体。第一个工作表包含图表，最后一个工作表包含一张图片，如下所示的截图。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|第一个工作表（销售预测）|第二个工作表（销售报告）|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|第三个工作表（数据录入）|最后一个工作表（图片）|

### **转换过程**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将电子表格呈现为 PDF 之前调用 [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) 方法。这样做可以确保重新计算依赖于公式的值，并在 PDF 中呈现正确的值。

{{% /alert %}}

### **结果**

运行以上代码后，将在您的应用程序目录中的Files文件夹中创建一个PDF文件。
以下截图显示PDF页面。请注意，页眉和页脚也保留在输出PDF文件中。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|第一个工作表（销售预测）|第二个工作表（销售报告）|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|第三个工作表（数据录入）|最后一个工作表（图片）|
