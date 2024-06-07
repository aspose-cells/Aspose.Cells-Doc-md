---
title: 将 Excel 图表转换为图像
type: docs
weight: 20
url: /zh/net/convert-an-excel-chart-to-image/
---

{{% alert color="primary" %}}

图表在视觉上具有吸引力，并使用户可以轻松查看数据中的比较、模式和趋势。例如，与分析工作表数字的列相比，图表一目了然地显示销售额是下降还是上升，或者实际销售额与预计销售额相比如何。人们经常被要求以易于理解和易于维护的方式呈现统计和图形信息，图片有助于这一点。

有时应用程序或网页需要图表。或者可能需要为 Word 文档、PDF 文件、PowerPoint 演示文稿或其他应用程序需要图表。在每种情况下，您希望将图表呈现为图像，以便在其他地方使用。

{{% /alert %}}

## **将图表转换为图像**

在这些示例中，将饼图和柱状图转换为图像。

### **将饼图转换为图像文件**

首先在 Microsoft Excel 中创建一个饼图，然后使用 Aspose.Cells 将其转换为图像文件。此示例中的代码基于模板 Microsoft Excel 文件创建一个 EMF 图像。

|**输出：饼图图像**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. 在 Microsoft Excel 中创建饼图：
   1. 在 Microsoft Excel 中打开一个新工作簿。
   1. 在工作表中输入一些数据。
   1. 基于数据创建一个饼图。
   1. 保存文件。

|**输入文件。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. 下载并安装Aspose.Cells:
   1. [下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)。
   1. 在开发计算机上安装它。

首次安装时，所有 [Aspose](http://www.aspose.com/) 组件均以评估模式运行。 评估模式没有时间限制，只会向输出文档中注入水印。

1. 创建一个项目:
   1. 启动 Visual Studio.Net。
   1. 创建一个新的控制台应用程序。 本示例使用的是 C# 控制台应用程序，但你也可以使用 VB.NET。
   1. 添加引用。 该项目使用了 Aspose.Cells，因此请添加对 Aspose.Cells 的引用，例如...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll。
   1. 编写代码以查找并转换图表。 以下是组件用来完成任务的代码。 仅使用了很少的代码行。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **将柱形图转换为图像文件**

首先在 Microsoft Excel 中创建一个柱形图，并将其转换为图像文件，如上所述。 执行示例代码后，将基于模板 Excel 文件中的柱形图创建一个 JPEG 文件。

|**输出文件：柱形图图像。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. 在 Microsoft Excel 中创建一个柱形图:
   1. 在Microsoft Excel中打开一个新的工作簿。
   1. 在工作表中输入一些数据。
   1. 根据数据创建一个柱形图。
   1. 保存文件。

|**输入文件。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. 按照上述描述设置一个项目，并添加引用。
1. 动态将图表转换为图像。 以下是组件用于完成任务的代码。 该代码与前面的代码类似。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
