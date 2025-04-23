---
title: 将XLSX文件转换为PDF格式
type: docs
weight: 30
url: /zh/net/convert-xlsx-file-to-pdf-format/
---

{{% alert color="primary" %}}

PDF（便携式文档格式）表示与用于创建这些文档的软件、硬件和操作系统无关。 PDF文件可以以一种与设备无关和与分辨率无关的方式表示任何组合的文本、图形和图像。 PDF文件通常是经过压缩的，因此占用的空间比原始文件少。

有时，您需要将Microsoft Excel文件转换为PDF。为此，您需要一种快速、安全、准确和可靠的解决方案，让您在全球范围内分发PDF文档。有许多可以执行此任务的转换工具。但您必须确保原始Excel文档的布局在输出PDF文件中得到保留。图像、图表、形状、数据格式、字体、属性、颜色、页面设置、文本方向、边框、图表等应该准确和精确地呈现。[Aspose.Cells](https://products.aspose.com/cells/net/)确保高保真度转换。

本文档旨在全面说明如何将Microsoft Excel文档（包含图像、图表、格式等）转换为PDF。为此，它展示了如何在Visual Studio .Net中创建一个简单的控制台应用程序，使用Aspose.Cells API将Excel文件转换为PDF。转换是以高度精确和准确性进行的。

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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

如果电子表格中包含公式，最好在呈现到PDF前调用 [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) 方法。这样可以确保重新计算基于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

### **结果**

当上述代码运行后，在应用程序目录的Files文件夹中创建了一个PDF文件。
以下屏幕截图显示了PDF页面。 请注意，页眉和页脚也在输出PDF文件中保留。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|第一个工作表 **（销售预测）**|第二个工作表 **（销售报告）**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|第三个工作表 **（数据录入）**|最后一个工作表 **（图像）**|
{{< app/cells/assistant language="csharp" >}}
