---
title: 将 Excel 图表转换为图像
type: docs
weight: 20
url: /zh/net/convert-an-excel-chart-to-image/
---
{{% alert color="primary" %}}

图表在视觉上很吸引人，使用户可以轻松查看数据中的比较、模式和趋势。例如，图表不是分析工作表数字的列，而是一目了然地显示销售额是下降还是上升，或者实际销售额与预计销售额的比较情况。人们经常被要求以易于理解和易于维护的方式呈现统计和图形信息。图片有帮助。

有时，应用程序或网页中需要图表。或者 Word 文档、PDF 文件、PowerPoint 演示文稿或其他一些应用程序可能需要它。在每种情况下，您都希望将图表呈现为图像，以便您可以在其他地方使用它。

{{% /alert %}}

## **将图表转换为图像**

在此处的示例中，饼图和列字符被转换为图像。

### **将饼图转换为图像文件**

首先，在Microsoft Excel中创建一个饼图，然后用Aspose.Cells将其转换为图像文件。本例中的代码根据模板Microsoft Excel文件中的饼图创建一个EMF图像。

|**输出：饼图图像**|
|:- |
|![待办事项：图片_替代_文本](convert-an-excel-chart-to-image_1.png)|

1. 在 Microsoft Excel 中创建饼图：
 1.在Microsoft Excel中打开一个新的工作簿。
 1. 在工作表中输入一些数据。
 1.根据数据制作饼图。
 1. 保存文件。

|**输入文件。**|
|:- |
|![待办事项：图片_替代_文本](convert-an-excel-chart-to-image_2.png)|

1. 下载并安装 Aspose.Cells：
   1. [下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. 在您的开发计算机上安装它。

全部[Aspose](http://www.aspose.com/)组件在首次安装时以评估模式工作。评估模式没有时间限制，它只在输出文档中注入水印。

1. 创建一个项目：
 1. 启动 Visual Studio.Net。
 1. 创建一个新的控制台应用程序。此示例使用 C# 控制台应用程序，但您也可以使用 VB.NET。
 1.添加引用。该项目使用Aspose.Cells 所以添加对Aspose.Cells的引用，例如...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1.编写查找和转换图表的代码。下面是组件用来完成任务的代码。使用的代码行很少。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **将柱形图转换为图像文件**

先在Microsoft Excel中创建一个柱状图，并转换成图片文件，如上。执行示例代码后，根据模板Excel文件中的柱形图创建一个JPEG文件。

|**输出文件：柱形图图像。**|
|:- |
|![待办事项：图片_替代_文本](convert-an-excel-chart-to-image_3.png)|

1. 在Microsoft Excel中创建柱形图：
 1.在Microsoft Excel中打开一个新的工作簿。
 1. 在工作表中输入一些数据。
 1.根据数据制作柱形图。
 1. 保存文件。

|**输入文件。**|
|:- |
|![待办事项：图片_替代_文本](convert-an-excel-chart-to-image_4.png)|

1. 如上所述，使用参考设置项目。
1. 将图表动态转换为图像。以下是组件用于完成任务的代码。代码与上一个类似：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
