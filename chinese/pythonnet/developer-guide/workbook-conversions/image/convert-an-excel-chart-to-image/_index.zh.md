---
title: 将 Excel 图表转换为图像
type: docs
weight: 20
url: /zh/python-net/convert-an-excel-chart-to-image/
description: 使用 Aspose.Cells for Python via .NET API 将 Excel 图表转换为图像。
keywords: Python Convert an Excel Chart to Image, Export an Excel Chart to Image in Python via NET, Python Save an Excel Chart to Image.
---
{{% alert color="primary" %}}

图表具有视觉吸引力，使用户可以轻松查看数据中的比较、模式和趋势。例如，图表不是分析工作表中的数字列，而是一目了然地显示销售额是下降还是上升，或者实际销售额与预计销售额的比较情况。人们经常被要求以易于理解和易于维护的方式呈现统计和图形信息。图片有帮助。

有时，应用程序或网页中需要图表。或者，Word 文档、PDF 文件、PowerPoint 演示文稿或其他应用程序可能需要它。在每种情况下，您都希望将图表呈现为图像，以便可以在其他地方使用它。

{{% /alert %}}

##  **将图表转换为图像**

在此示例中，饼图和柱形图被转换为图像。

###  **将饼图转换为图像文件**

首先，在 Microsoft Excel 中创建一个饼图，然后将其转换为带有 Aspose.Cells for Python via .NET 的图像文件。本示例中的代码根据模板 Microsoft Excel 文件中的饼图创建一个 EMF 图像。

|**输出：饼图图像**|
| :- |
|![待办事项：图像_替代_文本](convert-an-excel-chart-to-image_1.png)|

1. 在 Microsoft Excel 中创建饼图：
 1.在Microsoft Excel中打开一个新工作簿。
 1. 在工作表中输入一些数据。
 1. 根据数据创建饼图。
 1. 保存文件。

|**输入文件。**|
| :- |
|![待办事项：图像_替代_文本](convert-an-excel-chart-to-image_2.png)|

我们在 PyPi 存储库中托管 Python 包。

从 pypi 安装 Aspose.Cells for Python，使用命令为： $ pip install aspose-cells-python。

您还可以按照有关如何将“Aspose.Cells for Python via .NET”安装到开发环境的分步说明进行操作。
1. 下载并安装Aspose.Cells for Python via .NET：
 1.安装Aspose.Cells for Python via .NET[皮皮](https://pypi.org/project/aspose-cells-python/)，使用命令为：$ pip install aspose-cells-python。
 1.您还可以按照[分步说明](https://docs.aspose.com/cells/python-net/getting-started/)关于如何将“Aspose.Cells for Python via .NET”安装到您的开发环境。

全部[Aspose](http://www.aspose.com/)首次安装时，组件在评估模式下工作。评估模式没有时间限制，仅在输出文档中注入水印。

1. 创建一个项目：
 1. 启动 Visual Studio。
 1. 将库引用（导入库）添加到您的 Python 项目中。
 1. 编写查找并转换图表的代码。下面是组件用来完成任务的代码。使用的代码很少。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

###  **将柱形图转换为图像文件**

首先在Microsoft Excel中创建一个柱形图，并将其转换为图像文件，如上。执行示例代码后，会根据模板Excel文件中的柱形图创建一个JPEG文件。

|**输出文件：柱形图图像。**|
| :- |
|![待办事项：图像_替代_文本](convert-an-excel-chart-to-image_3.png)|

1. 在 Microsoft Excel 中创建柱形图：
 1. 在 Microsoft Excel 中打开一个新工作簿。
 1. 在工作表中输入一些数据。
 1. 根据数据创建柱形图。
 1. 保存文件。

|**输入文件。**|
| :- |
|![待办事项：图像_替代_文本](convert-an-excel-chart-to-image_4.png)|

1. 如上所述，设置一个带有参考的项目。
1. 动态地将图表转换为图像。以下是组件用来完成任务的代码。该代码与上一个类似：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
