---
title: 将Excel图表转换成图像
type: docs
weight: 20
url: /zh/python-net/convert-an-excel-chart-to-image/
description: 使用 Aspose.Cells for Python via .NET API 将 Excel 图表转换为图像。
keywords: Python 将 Excel 图表转换为图像，在 Python 中导出 Excel 图表为图像 via NET，Python 保存 Excel 图表为图像。
---

{{% alert color="primary" %}}

图表在视觉上很吸引人，可以帮助用户轻松地观察数据的比较、模式和趋势。例如，与分析工作表数字列相比，图表能够一眼看出销售额是下降还是上升，以及实际销售额与预期销售额的比较如何。人们经常需要以易于理解和维护的方式呈现统计和图形信息。图片有助于解释。

有时，在应用程序或网页中需要图表。或者可能需要将图表用于 Word 文档、PDF 文件、PowerPoint 演示文稿或其他应用程序中。在每种情况下，您希望将图表渲染为图像，以便在其他地方使用。

{{% /alert %}}

## **将图表转换为图像**

在这些示例中，饼图和柱状图被转换为图像。

### **将饼图转换为图像文件**

首先，在 Microsoft Excel 中创建一个饼图，然后使用 Aspose.Cells for Python via .NET 将其转换为图像文件。此示例中的代码基于模板 Microsoft Excel 文件中的饼图创建 EMF 图像。

|**输出：饼图图像**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. 在 Microsoft Excel 中创建一个饼图：
   1. 在 Microsoft Excel 中打开一个新工作簿。
   1. 在工作表输入一些数据。
   1. 根据数据创建一个饼图。
   1. 保存文件。

|**输入文件。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

我们将 Python 包托管在 PyPi 存储库中。

从 pypi 安装 Aspose.Cells for Python，请使用如下命令：$ pip install aspose-cells-python。

您还可以按照逐步说明来安装 “Aspose.Cells for Python via .NET” 到您的开发环境。
1. 下载并安装 Aspose.Cells for Python via .NET：
   从 [pypi](https://pypi.org/project/aspose-cells-python/) 安装 Aspose.Cells for Python via .NET，请使用如下命令：$ pip install aspose-cells-python。
   1. 您也可以遵循[逐步说明](https://docs.aspose.com/cells/python-net/getting-started/)，了解如何将"Aspose.Cells for Python via .NET"安装到您的开发环境中。

在首次安装时，所有[Aspose](http://www.aspose.com/)组件均以评估模式运行。 评估模式没有时间限制，只会向输出文档中注入水印。

1. 创建一个项目：
   1. 启动Visual Studio。
   1. 向您的Python项目添加库引用（导入库）。
   1. 编写查找并转换图表的代码。 以下是组件用于完成任务的代码。 使用的代码行很少。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

### **将柱状图转换为图像文件**

首先在Microsoft Excel中创建柱状图，然后将其转换为图像文件，如上所示。执行示例代码后，基于模板Excel文件中的柱状图创建了一个JPEG文件。

|**输出文件：柱状图图像。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. 在Microsoft Excel中创建柱状图：
   1. 在Microsoft Excel中打开一个新的工作簿。
   1. 在工作表输入一些数据。
   1. 根据数据创建柱状图。
   1. 保存文件。

|**输入文件。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. 配置项目及引用，如上所述。
1. 动态将图表转换为图像。 以下是组件用于完成任务的代码。 该代码与先前的代码类似。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
