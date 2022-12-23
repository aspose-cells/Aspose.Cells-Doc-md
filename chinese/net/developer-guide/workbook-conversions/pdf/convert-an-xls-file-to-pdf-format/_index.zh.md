---
title: 将 XLS 文件转换为 PDF 格式
type: docs
weight: 30
url: /zh/net/convert-an-xls-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF（便携式文档格式）表示独立于用于创建这些文档的软件、硬件和操作系统的文档。 PDF 文件可以是具有与设备无关和与分辨率无关的方式的文本、图形和图像的任意组合的文档。 PDF 文件经常被压缩，因此它们占用的空间比原始文件少。

有时，您需要将 Microsoft Excel 文件转换为 PDF。为此，您需要一个快速、安全、准确和可靠的解决方案，让您在世界各地分发 PDF 文档。有许多转换工具可以执行此任务。但是您必须确保原始 Excel 文档的布局保留在输出 PDF 文件中。图像、数据格式、字体、属性、颜色、页面设置、文本方向、边框、图表等都应该准确无误地呈现。[Aspose.Cells](https://products.aspose.com/cells/net/)确保高保真转换。

本文档旨在全面了解如何将 Microsoft Excel 文档（包含图像、图表、格式等）转换为 PDF。为此，展示了如何在 Visual Studio.Net 中创建一个简单的控制台应用程序来转换使用 Aspose.Cells API 将 Excel 文件转换为 PDF。转换以高精度和准确度执行。

{{% /alert %}}

## **将 Excel 转换为 PDF**

此示例使用 Excel 文件 (SampleInput.xlsx) 作为模板。该工作簿包含带有图表和图像的工作表。每个工作表都包含不同类型的格式，使用字体、属性、颜色、阴影效果和边框。第一个工作表上有一个柱形图，最后一个工作表上有一个图像。

### **模板 Excel 文件**

模板文件包含三个工作表，包括图表和图像作为媒体。第一个工作表有图表，最后一个工作表有一个图像，如下面的屏幕截图所示。

|![待办事项：图片_替代_文本](Convert_an_XLS_File_to_PDF_Sheet1.png)|![待办事项：图片_替代_文本](Convert_an_XLS_File_to_PDF_Sheet2.png)|
|:- |:- |
|第一张工作表**（销售预测）**|第二张工作表**（销售报告）**|
|![待办事项：图片_替代_文本](Convert_an_XLS_File_to_PDF_Sheet3.png)|![待办事项：图片_替代_文本](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|第三张工作表**（数据输入）**|最后一张工作表**（图片）**|

### **转换过程**

1. 下载并安装 Aspose.Cells：
 1.下载Aspose.Cells for .NET。
 1. 在您的开发计算机上安装它。
1. 创建项目并添加引用：
 1. 启动 Visual Studio.Net。
 1. 创建一个新的控制台应用程序。
1.添加对…\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll的引用
1. 将转换代码添加到项目中：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将电子表格呈现为 PDF 之前调用 Workbook.CalculateFormula()。这样做可确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

### **结果**

运行上述代码后，将在应用程序目录的 Files 文件夹中创建一个 PDF 文件。
以下屏幕截图显示了 PDF 页面。请注意，页眉和页脚也保留在输出 PDF 文件中。

|![待办事项：图片_替代_文本](Convert_an_XLS_File_to_PDF_Converted1.png)|![待办事项：图片_替代_文本](Convert_an_XLS_File_to_PDF_Converted2.png)|
|:- |:- |
|第一张工作表**（销售预测）**|第二张工作表**（销售报告）**|
|![待办事项：图片_替代_文本](Convert_an_XLS_File_to_PDF_Converted3.png)|![待办事项：图片_替代_文本](Convert_an_XLS_File_to_PDF_Converted4.png)|
|第三张工作表**（数据输入）**|最后一张工作表**（图片）**|
