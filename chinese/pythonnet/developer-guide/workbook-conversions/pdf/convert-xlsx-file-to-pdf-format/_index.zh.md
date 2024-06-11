---
title: 将XLSX文件转换为PDF格式
type: docs
weight: 30
url: /zh/python-net/convert-xlsx-file-to-pdf-format/
description: 学习如何使用Aspose.Cells for Python via .NET API将XLSX文件转换为PDF格式
keywords: Python将XLSX文件转换为PDF格式，使用Python将xlsx转换为pdf，使用Python保存xlsx为pdf，Python xlsx转pdf，Python中的xlsx转pdf格式
---

{{% alert color="primary" %}}

PDF（便携式文档格式）表示与用于创建这些文档的软件、硬件和操作系统无关。 PDF文件可以以一种与设备无关和与分辨率无关的方式表示任何组合的文本、图形和图像。 PDF文件通常是经过压缩的，因此占用的空间比原始文件少。

有时，您需要将Microsoft Excel文件转换为PDF。 为此，您需要一个快速、安全、准确且可靠的解决方案，可以让您在全球范围内分发PDF文档。 有许多可以执行此任务的转换工具。 但是您必须确保原始Excel文档的布局在输出PDF文件中保留。 图像、图表、形状、数据格式设置、字体、属性、颜色、页面设置设置、文本方向、边框、图表等应准确和精确地呈现。 [Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) 确保高保真度转换。

本文档旨在全面了解如何将Microsoft Excel文档（包含图像、图表、格式等）转换为PDF。 为此，它展示了如何在Visual Studio.Net中创建一个简单的控制台应用程序，使用Aspose.Cells for Python via .NET API将Excel文件转换为PDF。 转换具有高度的精度和准确性。

{{% /alert %}}

## **将Excel转换为PDF**

此示例使用Excel文件（SampleInput.xlsx）作为模板。 该工作簿包含具有图表和图像的工作表。 每个工作表都包含使用字体、属性、颜色、阴影效果和边框的不同类型格式。 第一个工作表上有一个柱状图，最后一个工作表上有一个图像。

### **模板Excel文件**

模板文件有三个工作表，包括图表和图像作为媒体。 第一个工作表有图表，最后一个工作表有一个图像，如下屏幕截图所示。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|第一个工作表 **（销售预测）**|第二个工作表 **（销售报告）**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|第三个工作表 **（数据录入）**|最后一个工作表 **（图像）**|

### **转换过程**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将电子表格渲染为PDF之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) 方法。 这样做可以确保重新计算以公式为依赖的值，并在PDF中呈现正确的值。

{{% /alert %}}

### **结果**

当上述代码运行后，在应用程序目录的Files文件夹中创建了一个PDF文件。
以下屏幕截图显示了PDF页面。 请注意，页眉和页脚也在输出PDF文件中保留。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|第一个工作表 **（销售预测）**|第二个工作表 **（销售报告）**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|第三个工作表 **（数据录入）**|最后一个工作表 **（图像）**|
